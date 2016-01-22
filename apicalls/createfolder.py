import requests
import sys, os
import json

#Create a new folder in a given folder directory in box.com
#Takes 2 arguments: 1. The new Folder name 2. The directory ID
#Example call:
#$ python createfolder.py NEW_FOLDER_NAME DIRECTORY_ID

if len(sys.argv) != 3: #first element is script name. 
    sys.exit("Aborting. This API takes 2 arguments: New_Folder_Name and Directory_ID - if not Directory_ID then type 0 after the folder name and the folder will be created at root")
else:
    flname = sys.argv[1]  #name given to new folder to be created through the API
    drid = sys.argv[2] #ID for directory in which folder would be created - if it equals "0" then it will create folder at root in box.com

data = "{\"name\":\""+flname+"\",\"parent\":{\"id\":\""+drid+"\"}}"

access_token = json.loads(open('../token/access_token.json').read())['access_token']

header = {'Authorization':'Bearer %s' % access_token,'content-type': "application/json"}

upload_url = "https://api.box.com/2.0/folders/"

resp = requests.post(upload_url, headers=header,data=data)
print("api call, response code: %s" % resp.status_code)
print(resp.text)