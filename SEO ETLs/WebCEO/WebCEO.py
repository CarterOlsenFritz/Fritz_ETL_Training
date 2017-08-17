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
#import urllib2 # DNE in python3?
import json

# API command to get the list of projects added to a user's account in Web CEO

command = {'key":'+api_key+',"method": "get_projects"'}

# Trying to find a way around "Object of type 'set' is not JSON serializable"
# https://stackoverflow.com/questions/9746303/how-do-i-send-a-post-request-as-a-json
# https://stackoverflow.com/questions/8230315/python-sets-are-not-json-serializable

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

# generate body of a POST request
myurl = "https://online.webceo.com/api/"
req = urllib.request.Request(myurl)
req.add_header('Content-Type', 'application/json; charset=utf-8')
jsondata = json.dumps(set(command), cls=SetEncoder)
jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
req.add_header('Content-Length', len(jsondataasbytes))
print (jsondataasbytes)
response = urllib.request.urlopen(req, jsondataasbytes)

responsetext = response.read()
text = responsetext.decode(encoding='utf-8',errors='ignore')

print(text)

#projects = json.load()
"""
# parse JSON response
projects = json.loads(response.read())[0]['data']

# print list of projects
for project in projects:
  print (project['domain'])
"""