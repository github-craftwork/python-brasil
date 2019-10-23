import os
import json
import requests

# event = json.loads(open(os.getenv('GITHUB_EVENT_PATH')))
# print event 

# comment = event["comment"]["body"]
comment = ".invite me"
team_id = 3414353
# commenter = event["comment"]["user"]["login"]
commenter = "notBdougie"

API_ENDPOINT = "https://api.github.com/organizations/55258788/public_members/" + commenter
API_ENDPOINT2 = "https://api.github.com/organizations/55258788/" + commenter

print("-------------------------------------------------")


if ".invite" in comment and len(comment.split()) == 2:
    r = requests.get(url = API_ENDPOINT)
    
    print("Member Status: " + r.status_code)

    if r.status_code == 200:
        exit(78)

    headers={'Authorization': os.getenv('GITHUB_TOKEN')}

    h = requests.post(url = API_ENDPOINT2, headers = headers)
    print("Invite: " + h.text)

print("-------------------------------------------------")

print("Action succesfully ran")
