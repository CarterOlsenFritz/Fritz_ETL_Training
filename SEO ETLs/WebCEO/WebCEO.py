# Example in Python 2.7 that prints a list of projects added to a Web CEO account:
# I've gotta update this for Python3

"""
# Raw original  sample from https://online.webceo.com/help-center/api/examples.html
import urllib
import urllib2
import json

# API command to get the list of projects added to a user's account in Web CEO
command = {"key": "YOUR_API_KEY", "method": "get_projects"}

# generate body of a POST request
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request("https://online.webceo.com/api/", data=urllib.urlencode({'json':
json.dumps(command)}))

# request data
response = opener.open(request)

# parse JSON response
projects = json.loads(response.read())[0]['data']

# print list of projects
for project in projects:
  print project['domain']
"""
from credentials_webceo import *
import urllib.request
import urllib.parse
import requests
#import urllib2 # DNE in python3?
import json
import webbrowser
import csv
import sys



# API command to get the list of projects added to a user's account in Web CEO

url = "https://online.webceo.com/api/"
#payload_showing_key = {'key':'API KEY GOES HERE', 'method': 'get_projects'} # This works only if I hardcode the API Key, and I'm not doing that shit.
#print(payload_showing_key)
#stringOfJsonData = json.dumps(payload_showing_key)
#print(stringOfJsonData)


payload_dict = {
    'key': api_key2,
    'method': 'get_projects'
}
print(payload_dict)
payload = json.dumps(payload_dict)
print(payload)

result = requests.post(url, data=payload)
print(result.text)
#r = requests.get(url, params=payload) # i duno what this does

"""
# This writes to a .json or .txt depending on how the file extension. Right now this is a .json file but filled with "result.text". I have no idea if this would be usable as a json. I think so since the text editor recognizes it.
handle = open("test.json", "w")
handle.write(result.text)
handle.close()
"""

#TODO: Learn how to write to a csv.
# Everything below here is garbage.
result_parsed = json.loads(result)
print(result_parsed)

#'data' is the first term in the json file. eg: [{"data":[{"project":"3cc5dac7"...

result_data = result_parsed['data']

# open a file for writing

json_data = open('json_data.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(json_data)

count = 0

for emp in json_data:
      if count == 0:
             header = emp.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(emp.values())
json_data.close()
#TODO: Learn how to write to a tsv.
"""
# Don't know if I can use any of this below here.
with open('output.tsv', 'w') as output_file:
    dw = csv.DictWriter(output_file, sorted(result[0].keys()), delimiter='\t')
    dw.writeheader()
    dw.writerows(result)
"""
#TODO: Learn how to write json format data into csv.
#TODO: Learn how to write json and csv data into SQL