import json

json_file = open('output/andreagaleazzi/result.json')
data = json.load(json_file)

print(json.dumps(data, indent=1))
