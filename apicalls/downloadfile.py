import requests
import sys
import json

#Downloads a given box.com file to your local machine.
#Takes 2 argument:
#1. File ID
#2. file name # doesn't have to be the same name but it does need to have the same file extension.

#Example call:
#$ python downloadfile.py 50894374961

if len(sys.argv) != 3: #first element is script name. 
    sys.exit("Aborting. You must provide file ID and a file name to download a file from box.com please try again")
else:
    fid = sys.argv[1]
    fname = sys.argv[2]

url = "https://api.box.com/2.0/files/"+fid+"/content"

access_token = json.loads(open('../token/access_token.json').read())['access_token']

header = {'Authorization':'Bearer %s' % access_token}

resp = requests.get(url, headers=header)
print("Initial api call to main folder, response code: %s" % resp.status_code)
if resp.status_code == 401:
    print ('Your access_token has expired refresh it with "refresh_access_token.py" script.')
if resp.status_code == 200:
    #print "file content ---:" # just used for testing
    #print(resp.text) # just used for testing
    file = open('files/downloaded/text2.xls','w') #testing hardcode file name
    file = open('files/downloaded/'+fname+'','w')
    file.write(resp.content)
    file.close()
    print "file downloaded successfully!"
if resp.status_code == 404:
    #print (resp.text)
    print ('Could not find the specified resource.')
    print ('Are you sure you have the correct file ID? Please try again.')