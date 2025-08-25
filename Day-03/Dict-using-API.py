import requests
import os
import pandas as pd

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json()  # Return the JSON data as a dictionary
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None
    
def Export_to_Excel(data, filename):
    if data is None:
        print("No data to export.")
        return

    rows = []
    for item in data:
        if isinstance(item, dict) and 'title' in item and 'user' in item and 'id' in item:
            rows.append({'Author': item['user']['login'], 'Title': item['title'], 'ID': item['id']})

    df = pd.DataFrame(rows, columns=['Author', 'Title', 'ID'])
    output_path = os.path.join(os.path.dirname(__file__), filename)
    if os.path.exists(output_path):
        os.remove(output_path)  # Remove the file if it already exists
        print(f"Existing file {filename} removed.")
    else:
        print(f"File {filename} does not exist, creating a new one.")
    df.to_excel(output_path, index=False)
    print(f"Data exported to {output_path}")

def main():
    url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
    data = fetch_data_from_api(url)
    Export_to_Excel(data, "pull_requests.xlsx")

if __name__ == "__main__":
    main()