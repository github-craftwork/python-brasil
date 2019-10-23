import os
import json
import requests

event = open(os.getenv('GITHUB_EVENT_PATH'), "r")
print(event.read())


print("-------------------------------------------------")

print("Action succesfully ran")
