# This code will list all projects in a Jira instance using Jira's REST API.

import requests
from requests.auth import HTTPBasicAuth
import json

url = "<Replace this with your-domain.atlassian.net>/rest/api/3/project"
API_TOKEN = "<Replace this with your API token>"

auth = HTTPBasicAuth("lpavanshetty818@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
for project in output:
    print(f"Project Name: {project['name']}, Project Key: {project['key']}")