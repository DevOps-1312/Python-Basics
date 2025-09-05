import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='pavan-test-bucket-1234567890',
)

print(response)
print("Bucket Created Successfully")