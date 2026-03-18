import json

# load the JSON data from the file
with open('company_data.json', 'r') as file:
    # parse the JSON data into a Python dictionary
    data = json.load(file)
    # json.loads() if parse a string of json data

# access the data
# simple key access
print(data['company_name'])  # Output: TechNova Solutions
# nested access
print(data['employees'][0]['name'])  # Output: Alice Chen

# modify the data locally
data['company_name'] = 'TechNova Global'
# add new key value pair
data['founded_year'] = 2010

# write the modified data back to the file
with open('company_data.json', 'w') as file:
    # convert dictionary back to json and save
    json.dump(data, file, indent=4)  # indent for pretty printing