"""This code parses a JSON text and edits the text using the python
    dict and converts the python-edit back to JSON text"""

import json

"""Opens the file and parses the text in a json format"""
with open("service_policy.json", "r") as file_read:
    policy = json.load(file_read)

"""changes the value for the Resource key using the python dict method"""
policy["Statement"]["Resource"] = "S3"

"""converts the python dict method edit back to a json format"""
with open("service_policy.json", "w") as file_updated:
    json.dump(policy, file_updated)


