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

API_ENDPOINT1 = "https://api.github.com/organizations/55258788/public_members/" + commenter
API_ENDPOINT2 = "https://api.github.com/users/" + commenter
API_ENDPOINT3 = "https://api.github.com/orgs/github-craftwork/invitations"

event = os.getenv('GITHUB_EVENT_PATH')
print(event)

print("-------------------------------------------------")


if ".invite" in comment and len(comment.split()) == 2:
    r = requests.get(url = API_ENDPOINT1)

    if r.status_code == 200:
        exit(78)

    p = requests.get(url = API_ENDPOINT2)

    id = p.json()['id']
    print("ID: " + str(id))

    headers={'Authorization': os.getenv('GITHUB_TOKEN'),
             'Accept': 'application/vnd.github.dazzler-preview+json'}
    data = {"invitee_id": id, "team_ids": [3484670]}

    h = requests.post(url = API_ENDPOINT3, data = json.dumps(data), headers = headers)
    print(h.text)

print("-------------------------------------------------")

print("Action succesfully ran")
