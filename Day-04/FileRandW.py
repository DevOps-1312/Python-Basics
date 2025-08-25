import os

def update_server_config(file_path, key, value):

    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        for line in lines:
            if line.startswith(key):
                file.write(f"{key}={value}\n")
            else:
                file.write(line)
    print(f"Updated {key} to {value} in {file_path}")

if __name__ == "__main__":
    key = input("Enter the key to update: ")
    value = input("Enter the new value: ")
    update_server_config("server.conf", key , value)
