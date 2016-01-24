import requests
import sys, os
import json

#Upload a local file to a box.com folder
#Takes three arguments: 1. filepath to be uploaded 2. destination folder ID 3. existing file id
#Example call:
#$ python ~/path_to_file.file.txt 1234567 7654321


if len(sys.argv) != 3: #first element is script name. 
    sys.exit("Aborting. You must provide in this order: filename path and folder id")
else:
    fname = sys.argv[1]
    fid = sys.argv[2]

data = {"parent_id": fid}
files = {"filename": open(fname,'rb') } #fid is name of folder in box you are uploading to. fname is name of file to upload (given as argument). 

access_token = json.loads(open('../token/access_token.json').read())['access_token']

header = {'Authorization':'Bearer %s' % access_token}

upload_url = "https://upload.box.com/api/2.0/files/content"

resp = requests.post(upload_url, headers=header,data=data,files=files)
print("api call, response code: %s" % resp.status_code)
if resp.status_code == 401:
    print ('Your access_token has expired refresh it with "refresh_access_token.py" script.')
#print(resp.text)
contentresp = resp.text

def get_file_id(content):
    finding_file_id = content.find('"file","id"')
    if finding_file_id == -1: 
        return None, 0
    start_file_id = content.find('"file","id"', finding_file_id) + 13
    end_file_id = content.find('"', start_file_id + 1)
    file_id = content[start_file_id:end_file_id]
    print ('File ID = ' + file_id)
    return file_id, end_file_id
if resp.status_code == 201:
    print ('File uploaded succesfully!!!')
if resp.status_code == 404:
    print ('It appears that you have used and Invalid Directory ID parameter.')
    print ('Please try again')
if resp.status_code == 409:
    print ('It appears that this file or a file with the same name has already been uploaded')
    print ('Did you mean to do that? - If not Please try again')

get_file_id(contentresp)



