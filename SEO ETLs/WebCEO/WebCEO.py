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

r = requests.post(url, data=payload)
print(r.text)
#r = requests.get(url, params=payload) # i duno what this does
"""
# This writes to a .json or .txt depending on how the file extension. Right now this is a .json file but filled with "r.text". I have no idea if this would be usable as a json. I think so since the text editor recognizes it.
handle = open("test.json", "w")
handle.write(r.text)
handle.close()
"""




#with open("requests_results.html","wb") as f:
#    f.write(r.content)
#webbrowser.open("results.html")

