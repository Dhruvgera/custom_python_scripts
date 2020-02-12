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
listdevice=["beryllium"]

n=len(listdevice)

for i in range(0,n):
	devicename=listdevice[i]
# Largest file finder
objects = os.listdir("out/target/product/"+devicename+"/") # Replace with the dir you want to search in

sofar = 0
name = ""

for item in objects:
        size = os.path.getsize("out/target/product/"+devicename+'/'+item) 
        if size > sofar:
                sofar = size
                name = item

# Sourceforge or any other sftp client uploader script

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
	print("Connection successful")

        # Switch to a remote directory
	sftp.cwd('/home/frs/project/pococustomroms/lineageos')  # Add your dir here
        # Obtain structure of the remote directory 
	directory_structure = sftp.listdir_attr()

        # Print data
	for attr in directory_structure:
        	print (attr.filename, attr)

	localFilePath = ("out/target/product/"+devicename+"/"+name) # The path where your file is stored on your drive
	remoteFilePath = (name) # The path where you want to upload
	sftp.put(localFilePath, remoteFilePath)
