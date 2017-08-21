#Update sys.path.insert for your credential document directory.
import sys
sys.path.insert(0, 'C:/Users/Carter/repos/Fritz_ETL_Training/SEO ETLs/WebCEO')
from credentials_webceo import *
import urllib.request
import urllib.parse
import requests
#import urllib2 # DNE in python3?
import json
import webbrowser
import csv




# Payload for 'get_rankings'
# project_id is 1:1 with each domain name, a list of them are in the original query results.
# History Depth needs to change if we want older data. AND if we only use history_depth = 1, what happens if the scan is the same data as the previous one? Should we just overwrite the old data? Or I could be smart and see that they match and then upload nothing. I think overwriting each day will give me a clear history of when an upload succesfully occurred or not; e.g.: easier for error spotting.
project_id = "ea6de9c0"
payload_dict = {
  'method': 'get_rankings',
  'key': api_key2,
  'data': {
    'project': project_id,
    'grouped': 0,
    'competitors': 0,
    'history_depth': 2
  }
}

payload = json.dumps(payload_dict)
url = "https://online.webceo.com/api/"
result = requests.post(url, data=payload)
result_parsed = json.loads(result.content)

# Option 3 for printing to a file as a PRETTY JSON
with open("Kirkus_get_rankings.json", "w") as f: #ending with 2 means history_depth of 2. I didnt see any difference though. /shrug
    f.write(json.dumps(result_parsed, indent=2))
#shutil.move(src, dst, copy_function=copy2) # for if i want to move from this directory to one specifically for Kirkus.

json2_data = result_parsed[0]['data'] # not sure if this will work since the resulting JSON isn't flat.
print(json2_data)
# This pull falls apart right here. I think I need to flatten the json. Maybe look into PANDAS for forcing into tabular format. https://github.com/amirziai/flatten + PANDAS looks to be a winner.
"""
json_to_csv = open('Kirkus_get_rankings.csv', 'w', newline='') # open a file for writing. newline='' is required to kill the line spacing generated in Windows machines.
csvwriter = csv.writer(json_to_csv)# create the csv writer object
count = 0 #start at 0

for data in json2_data:
      if count == 0:
             header = data.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(data.values())
json_to_csv.close()
"""