import boto3

client = boto3.client('s3')

response = client.get_bucket_acl(
    Bucket='pavan-test-bucket-1234567890',
)
print(response)
print("--------------------------------------------------------------")
print("total number of ACL's:", len(response))
print("---------------------------------------------------------------")
print("Owner Details:")
print("ID:", response['Owner']['ID'])
print("DisplayName:", response['Owner']['DisplayName'])
print("---------------------------------------------------------------")
