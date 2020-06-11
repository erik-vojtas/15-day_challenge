import json

data = {}
data['people'] = []
data['people'].append({
    'name': 'Scott',
    'website': 'stackabuse.com',
    'from': 'Nebraska'
})
data['people'].append({
    'name': 'Larry',
    'website': 'google.com',
    'from': 'Michigan'
})
data['people'].append({
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
})

with open('data.txt', 'w') as outfile:
    json.dump(data, outfile) #write


with open('data.txt') as infile:
    data = json.load(infile) #read
    for p in data['people']:
        print('Name: ' + p['name'])
        print('Website: ' + p['website'])
        print('From: ' + p['from'])
        print('')

print("-----------------------------------------")

dict = {1:"one", 2:"two"}
with open('data.json', 'w') as json_file:
    json.dump(dict, json_file)

with open('data.json') as json_file:
    my_data = json.load(json_file, )
    print(my_data)


print("-----------------------------------------")

json_data = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
            '{"ID":20,"Name":"David Lee","Role":"Editor"}]'

json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent=2)
print(json_formatted_str)

print("-----------------------------------------")