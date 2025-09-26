# This code will create a new issue in a Jira project using Jira's REST API.

import requests
from requests.auth import HTTPBasicAuth
import json

url = "<Replace this with your-domain.atlassian.net>/rest/api/3/issue"
API_TOKEN = "<Replace this with your API token>"

auth = HTTPBasicAuth("lpavanshetty818@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket.",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "issuetype": {
      "id": "10006"
    },
    "project": {
      "key": "SCRUM"
    },
    "summary": "First Jira issue",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))