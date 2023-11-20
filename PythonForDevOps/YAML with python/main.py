import yaml, pprint
with open("verify_apache.yaml", "r") as file:
    verify_apache = yaml.safe_load(file)

pprint.pprint(verify_apache)
