# Copyright (C) 2020 Dhruv Gera
import subprocess
import select
import os
import pysftp
import sys
import glob

# Your particulars for accessing the sftp client
myHostname = "frs.sourceforge.net"
myUsername = "your username"
myPassword = "your password"

# Device name is here for rom builds, as we need it in the out folder's name
devicename="sampledevice"

# Zip finder
objects = os.listdir("out/target/product/"+devicename+"/obj/PACKAGING/target_files_intermediates/") # Replace with the dir you want to search in

for file in os.listdir("out/target/product/"+devicename+"/obj/PACKAGING/target_files_intermediates/"):
    if file.endswith(".zip"):
        print(file)
os.environ["largest"] = file
# Sourceforge or any other sftp client uploader script

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
	print("Connection successful")

        # Switch to a remote directory
	sftp.cwd('/home/pfs/project/cygnus-android/test/')  # Add your dir here
        # Obtain structure of the remote directory 
	directory_structure = sftp.listdir_attr()

        # Print data
	for attr in directory_structure:
        	print (attr.filename, attr)

	localFilePath = ("out/target/product/"+devicename+"/obj/PACKAGING/target_files_intermediates/"+file) # The path where your file is stored on your drive
	remoteFilePath = (file) # The path where you want to upload
	sftp.put(localFilePath, remoteFilePath)

os.system("$PWD/upload.sh")
