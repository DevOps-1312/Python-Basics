# StringOperation.py
# String operations and manipulations in Python

arn = "arn:aws:iam::123456789012:user/example-user"
username = arn.split("/")[1]  # Extracts the last part of the ARN
print("Username extracted from ARN:", username)

print("-----------------------------------------------------------------------")

name = "Abhishek Kumar"
print("Original name:", name)
print("Name in title case:", name.title())
print("Name in uppercase:", name.upper())
print("Name in lowercase:", name.lower()) 

print("-----------------------------------------------------------------------")

str1 = "Hello"
str2 = "World"
print("Concatenated string:", str1 + " " + str2)
print("Length of concatenated string:", len(str1 + " " + str2))

print("-----------------------------------------------------------------------")

str3 = "**Python is fun**"
print("Original string:", str3)
print("Reversed string:", str3[::-1])
print("String after replacing 'fun' with 'awesome':", str3.replace("fun", "awesome"))
print("String split into words:", str3.split())
print("String after stripping whitespace:", str3.strip("*"))

print("-----------------------------------------------------------------------")