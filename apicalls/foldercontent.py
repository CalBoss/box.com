import requests
import sys, os
import json  # will add pretty print nested hash

#lookup folder content for a give folder/subfolder
#Takes 1 argument: 1. Folder ID

#Example call:
#$ python foldercontent.py 6213428277

if len(sys.argv) != 2: #first element is script name. 
    sys.exit("Aborting. You must provide subfolder ID to view files inside that folder in box.com")
else:
    fid = sys.argv[1]

# fid = "6213428277" #paste in manually here the folder ID you want to lock. Available from the URL on box.com

access_token = json.loads(open('../token/access_token.json').read())['access_token']

header = {'Authorization':'Bearer %s' % access_token}

fold_url = "https://api.box.com/2.0/folders/%s/items?"

#For a given folder (fid), list all the files in that folder. 

resp = requests.get(fold_url % fid, headers=header)
print("Initial api call to main folder, response code: %s" % resp.status_code)
files = resp.json()['entries']
#print files
content=(json.dumps(files,indent=1)) # Convert JSON to Python nested dictionary/list & "indent=1" will print nested hash
print(content)
#files = resp.json()['entries'][0:1] #to test, use [10:11] here to pick only the 11th file say.