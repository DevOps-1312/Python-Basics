import os

def list_files_in_folder(folder):
    try:
        files = os.listdir(folder)
        return files, None
    except FileNotFoundError:
        return None, f"Folder '{folder}' does not exist. Please provide a valid folder name."
    except PermissionError:
        return None, f"Permission denied to access folder '{folder}'."
    except Exception as e:
        return None, f"An error occurred while accessing folder '{folder}': {e}"

def main():
    folders = input("Enter the names of folders with space in between: ").split()
    for folder in folders:
        files, error = list_files_in_folder(folder)
        if error:
            print(error)
            continue
        if not files:
            print(f"Folder '{folder}' is empty.")
            continue
        print(f"==============Listing files in folder '{folder}' ===============:")
        for file in files:
            print(file)

if __name__ == "__main__":
    main()
