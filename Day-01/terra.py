# terra.py
# This script initializes a Terraform configuration in a specified directory.
import subprocess

def terraform_init(command):
    process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
    return process.stdout.decode()

directory = r"C:\Users\p.kumar.l\Documents\DevOps\Python-WorkShop\terraform"
command = f"terraform -chdir={directory} init"

output = terraform_init(command)
print(output)



