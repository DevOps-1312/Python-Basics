# loops.py
#list -> data structure which can hold multiple values of multiple data types and mutable.
#string -> data structure which can hold multiple values of same data type but immutable.
#array -> data structure which can hold multiple values of same data type.
#tuple -> data structure which can hold multiple values of multiple data types but immutable.
#dictionary -> data structure which can hold multiple values of multiple data types in key-value pair.
#sets -> data structure which can hold multiple values of same data type but unordered and unindexed
#loops -> used to iterate over a sequence (list, tuple, dictionary, set, string) or other iterable objects.
list_of_cloud = ["AWS", "Azure", "GCP", "IBM Cloud", "Oracle Cloud"]
print("List of Cloud Providers: ", list_of_cloud)

# add a new cloud provider to the list
list_of_cloud.append("Cloudflare")
print("List after appending a new cloud provider: ", list_of_cloud)
print("-----------------------------------------------------------------------")

# add a new cloud provider to the list at a specific index
list_of_cloud.insert(2, "Tencent Cloud")
print("List after inserting 'Tencent Cloud' at index 2: ", list_of_cloud)
print("-----------------------------------------------------------------------")

# insert "Hello cloud" at the beginning of the list
list_of_cloud.insert(0, "Hello Cloud")
print("List after inserting 'Hello Cloud' at 0th index: ", list_of_cloud)
print("-----------------------------------------------------------------------")

# iterate over the list and print each cloud provider
print("Iterating over the list of cloud providers:")
for cloud in list_of_cloud:
    print(cloud)
print("-----------------------------------------------------------------------")

for i in range(len(list_of_cloud)):
    print(f"Cloud provider at index {i}: {list_of_cloud[i]}")