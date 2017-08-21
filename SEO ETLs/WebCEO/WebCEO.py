"""
# Example in Python 2.7 that prints a list of projects added to a Web CEO account:
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
#print(payload_dict) # prints as a single quoted payload
payload = json.dumps(payload_dict)
#print(payload) # prints as a double quoted payload

result = requests.post(url, data=payload)
#print(result.text) # Returns a working JSON, but as a list. with double quotes
#print(result.json()) # Returns a working JSON, but as a list. with single quotes
#print(result.content) # THIS RETURNS BINARY DATA. CAN I USE IT?




"""
# This writes to a .json or .txt depending on how the file extension.
# JSONlint.com recognizes all of these as valid JSON.
# Option 1. Prints on one line.
handle = open("data.json", "w")
handle.write(result.text)
handle.close()

# Option 2 Prints on one line.
with open("data2.json", "wb") as f:
    f.write(result.content)
"""



#############################################################
# How to extract relevant JSON "data" and write to a CSV.
# First lines show how to indent JSON output.
#############################################################
# This block establishes the server response in a pretty format.
result_parsed = json.loads(result.content)
#print(json.dumps(result_parsed, indent=4)) # This is a test print of JSON data in a pretty format. It can only be written as "w", not "wb".

"""
# Option 3 for printing to a file as a PRETTY JSON 
with open("data3.json", "w") as f:
    f.write(json.dumps(result_parsed, indent=2))
"""

#'data' is the first term in the json file. eg: [{"data":[{"project":"3cc5dac7"...
#result_data = result_parsed["data"] #This data is apparently a LIST with only 1 value.
"""
json1_data = result_parsed[0] # Get the first value of the array.
data = json1_data['data'] #Now I can specify to just a particular object. In this test case: 'data'.
#print(data) #printing results to confirm. 
"""
json2_data = result_parsed[0]['data'] # A condensed form of the block directly above.
#print(json2_data)



json_to_csv = open('json_data.csv', 'w', newline='') # open a file for writing. newline='' is required to kill the line spacing generated in Windows machines.
csvwriter = csv.writer(json_to_csv)# create the csv writer object
count = 0 #start at 0

for data in json2_data:
      if count == 0:
             header = data.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(data.values())
json_to_csv.close()

print("         bottom of file") # my place marker in console to make sure everything executed in new code additions.

#############################################################
#TODO: Learn how to write to a tsv.
#############################################################
"""
# Don't know if I can use any of this below here.
json_to_tsv = open('output.tsv', 'w', newline='') # open a file for writing. newline='' is required to kill the line spacing generated in Windows machines.
csvwriter = csv.writer(json_to_tsv)# create the csv writer object
count = 0 #start at 0

for data in json2_data:
      if count == 0:
             header = data.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(data.values())
json_to_tsv.close()

with open('output.tsv', 'w') as output_file:
    dw = csv.DictWriter(output_file, sorted(json2_data.keys()), delimiter='\t')
    dw.writeheader()
    dw.writerows(json2_data)

with open('output.tsv', 'w') as output_file:
    dw = csv.DictWriter(output_file, sorted(json2_data), delimiter='\t')
    dw.writeheader()
    dw.writerows(json2_data)

input_file = csv.DictReader(open("json_data.csv"))
for row in input_file:
    print(row)
"""

    #############################################################
#TODO: Learn how to write JSON and csv data into SQL via SQLalchemy or some other option.
#############################################################