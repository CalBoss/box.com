API calls for box.com
=======

#Token Setup
0. An app associated with your box.com account first needs to be created through the box developers site: (https://app.box.com/developers/services). Set the redirect URL to be https://127.0.0.1
1. After cloning this repository, create the subfolder box.com/token. This folder will hold your client ID and client Secret, along with access token when generated. Do not make this folder public in any way (for example, never push this folder to github!)
2. Within the subfolder, create a simple text file and call it client.txt containing two lines (client_id and client_secret need to be copied from the application page):
```
cid = "paste in your client id here"
cpw = "paste in your client secret here'
```
3. Now it's time to generate a token. Paste the client_id into the link below, and access the website.
 
	[Click this link to generate launch box login and generate first authorization code](https://app.box.com/api/oauth2/authorize?response_type=code&client_id=PASTE_CLIENT_ID_HERE&state=security_token%random_string_987654321 "Box.com login")

	you will have to replace the "[PASTE_CLIENT_ID_HERE]" with your own Box configured application's "client_id".
```
https://app.box.com/api/oauth2/authorize?response_type=code&client_id=[PASTE_CLIENT_ID_HERE]&state=security_token%random_string_987654321
```
 
4. After logging in and authorizing your app by clicking on the <p><image src="https://download.trstone.com/productsupport/images/grant_access_to_box.png"></p> button, you will then see this:

	<p align="center"><img src="https://download.trstone.com/productsupport/images/box_autho_code.png" width="650"/></p>

	Copy the Authorization code from the address bar, and paste it as a single argument as shown below.
```
python get_access_token.py "pastecodefromlinkabovehere"
```
5. That's it. It is now easy to refresh your applications credentials without any more mucking around. Just run:
```
python refresh_access_token.py
```
NOTE: For More info on how to complete the above initial process for your local app watch this video:  https://www.youtube.com/watch?v=ha26tN8amI0

<hr>

#API Calls

##Create a Folder
This script Creates a Folder inside a given directory. it takes 2 arguments in this order:
* Name of new folder
* Destination folder ID
```
python box.com/apicalls/createfolder.py [NAME_OF_NEW_FOLDER DESTINATION_OF_DIRECTORY_ID] 
```

##Upload a file
This script uploads a local file to your box.com account. Useful for uploading new files to a remote box folder. This script takes 2 arguments in this order:
* Local system filepath with filename
* Box.com Destination ID folder [Using 0 would place files at root]
```
python box.com/apicalls/uploadfile.py /local_path/to/file.txt [BOX_DEST_FOLDER_ID]
```
##Update a file
This script uploads a local file to your box.com account. Useful for automating backups. This script takes 2 arguments in this order:
* local system filepath with filename
* File ID for the file you want to update
```
python box.com/apicalls/updatefile.py /local_path/to/file.txt [BOX_EXIST_FILE_ID] 
```
NOTE: Make sure you use the same extension as the file you would like to update.
##View folder Content
This script will give you all content file information in a given folder. This script takes only one arguement:
* Folder ID for the folder you want to look up.
```
python box.com/apicalls/foldercontent.py [BOX_EXIST_FOLDER_ID]
```
##Download a file
This script downloads a given file from box.com. This script takes 2 arguments in this order:
* File ID for the file you want to download
* File name with the corresponding file extention. It doesn't necessarily have to be the same name but it must be have the same extention. Changing the extenstion from the original file in Box will either corrupt or distroy it's content.
* File would be downloaded to a destination directory called "Downloads/" it will auto create the directory if not in place.

NOTES:  
	the autocreation of the downloads folder has only been tested in 2.7.11 python on OS X 10.11.  since the script is hard coded to this path you will have to update the script to make it work with our own destination directory.
	If you use a file name for a file already in the destination folder then its content would be overwritten by the content of file being used in the API.
```
python box.com/apicalls/downloadfile.py [FILE ID #] filename
```
##Lock files [ Not currently working it has a bug]
This script locks or unlocks all the files in a given folder (including all the sub folders, and sub-sub folders etc.)
```
python box.com/apicalls/lockfiles.py
```
##Monitor Events [Still not working]
A script to monitor events on a given folder in box.com. It will print to screen certain 'allowed' or 'disallowed' events as detailed in whitelist.py. The script is designed to be deployed through cron, every workday, say, at 9am.
```
python box.com/apicalls/monitor/print_events.py
```
```
0 9 * * 1-5	python ~/box.com/apicalls/monitor/print_events.py
```
still in testing
