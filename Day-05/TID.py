import os
import random
import string
import shutil
import xml.etree.ElementTree as ET

def random_transaction_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

def random_claim_number():
    return '{:07d}'.format(random.randint(0, 9999999))

def process_xml(input_path, attr_map, output_path):
    try:
        tree = ET.parse(input_path)
        root = tree.getroot()
        changed = False
        for elem in root.iter():
            for attr, value in attr_map.items():
                if attr in elem.attrib:
                    elem.set(attr, value)
                    changed = True
        if not changed:
            print(f"Warning: No attributes replaced in {input_path}")
        tree.write(output_path, encoding='utf-8', xml_declaration=True)
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

def main():
    generic_file = 'GENERIC_ROUGHDRAFT.xml'
    xactdoc_file = 'XACTDOC.XML'
    output_dir = 'Output'
    if not (os.path.isfile(generic_file) and os.path.isfile(xactdoc_file)):
        print("Required XML files not found in the current directory.")
        return
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    try:
        N = int(input("Enter the number of sets to generate (positive integer): "))
        if N <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        return
    generated_files = []
    for i in range(N):
        transaction_id = random_transaction_id()
        claim_number = random_claim_number()
        # GENERIC_ROUGHDRAFT.xml
        generic_out = f"GENERIC_ROUGHDRAFT_{transaction_id}.xml"
        process_xml(
            generic_file,
            {'transactionId': transaction_id, 'claimNumber': claim_number},
            generic_out
        )
        generated_files.append(generic_out)
        # XACTDOC.XML
        xactdoc_out = f"XACTDOC_{claim_number}.xml"
        process_xml(
            xactdoc_file,
            {'transactionID': transaction_id, 'claimNumber': claim_number},
            xactdoc_out
        )
        generated_files.append(xactdoc_out)
    # Move files to Output folder
    for file in generated_files:
        shutil.move(file, os.path.join(output_dir, file))
    print(f"All generated files have been moved to the '{output_dir}' folder.")

if __name__ == "__main__":
    main()
