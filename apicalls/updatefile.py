import requests
import sys, os
import json

#Upload a local file to a box.com folder
#Takes three arguments: 1. filepath to be uploaded 2. destination folder ID 3. existing file id
#Example call:
#$ python ~/path_to_file.file.txt 1234567 7654321
def get_file_id(content):  # a function to extract the assigned file ID
    finding_file_id = content.find('"file","id"')
    if finding_file_id == -1: 
        return None, 0
    start_file_id = content.find('"file","id"', finding_file_id) + 13
    end_file_id = content.find('"', start_file_id + 1)
    file_id = content[start_file_id:end_file_id]
    print ('File ID = ' + file_id)
    return file_id, end_file_id

def get_file_version(content):  # a function to extract the assigned file ID
    finding_file_version = content.find('"etag":"')
    if finding_file_version == -1: 
        return None, 0
    start_file_version = content.find('"etag":"', finding_file_version) + 8
    end_file_version = content.find('"', start_file_version + 1)
    version = (content[start_file_version:end_file_version])
    a = str('1')    # For some reason the value given by the API is on version behind what is shown in box.com for the given file version
    file_version = int(a) + int(version) 
    print 'Label as Version =',file_version
    return file_version, end_file_version

if len(sys.argv) != 3: #first element is script name. 
    sys.exit("Aborting. You must provide in this order: filename path and folder id and existing file id (so it can be replaced)")
else:
    fname = sys.argv[1]
    #flid = sys.argv[2] #if uncommenting this line then you will need to change 3 to 4 in line 19
    flid = 0
    exist_id = sys.argv[2]#originally 3 since flid used to be obtained through commented line 23

data = {"parent_id": flid}#flid is name of folder in box you are uploading to. fname is name of file to upload (given as argument). 
files = {"filename": open(fname,'rb') }

access_token = json.loads(open('../token/access_token.json').read())['access_token']

header = {'Authorization':'Bearer %s' % access_token}

upload_url = "https://upload.box.com/api/2.0/files/%s/content"

#this next line is the original one that used the 3 argument that doesn't seem to matter when updating a file
resp = requests.post(upload_url % exist_id, headers=header,data=data,files=files)
#resp = requests.post(upload_url, headers=header,data=data,files=files)
print("api call, response code: %s" % resp.status_code)
if resp.status_code == 401:
    print ('Your access_token has expired refresh it with "refresh_access_token.py" script.')
#print(resp.text) # used for testing It will give the entire response message back from the API
#print type(resp.text)
contentresp = resp.text

if resp.status_code == 201:
    print ('File updated succesfully!!!')
if resp.status_code == 404:
    print ('It appears that you have used and Invalid Directory ID parameter.')
    print ('Please try again')
if resp.status_code == 409:  # this was originally a status code extracted from updloadfile.py script not sure if it's right
    print ('It appears that this file or a file with the same name has already been uploaded')
    print ('Did you mean to do that? - If not Please try again')

get_file_id(contentresp)
get_file_version(contentresp)

