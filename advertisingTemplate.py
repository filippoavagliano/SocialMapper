import json

f = open('result.json')

profile = json.load(f)

logos = {}

logos = profile['logohunter']

logosSorted = sorted(logos.items(), key = lambda x : x[1],reverse=True)
converted_dict = dict(logosSorted)
print(converted_dict)

'''
for i in profile['logohunter']:
    #print(i)
    logos.append(i)

print(logos)
'''



f.close()
