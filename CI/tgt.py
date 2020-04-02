# Copyright (C) 2020 Dhruv Gera
import subprocess
import select
import os
import pysftp
import sys
import glob

usr=os.environ["SF_USR"]
passw=os.environ["SF_PASS"]
# Your particulars for accessing the sftp client
myHostname = "frs.sourceforge.net"
myUsername = usr
myPassword = passw

# Device name is here for rom builds, as we need it in the out folder's name
devicename="sampledevice"
os.system("cd out/target/product/sampledevice/obj/PACKAGING/target_files_intermediates/ && rm -R -- */ && rm *list ")

# File finder
d="out/target/product/"+devicename+"/obj/PACKAGING/target_files_intermediates"
for path in os.listdir(d):
    full_path = os.path.join(d, path)
    if os.path.isfile(full_path):
        print(full_path)

head, tail = os.path.split(full_path)
os.environ["largest"] = tail

# Sourceforge or any other sftp client uploader script

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword) as sftp:
	print("Connection successful")

        # Switch to a remote directory
	sftp.cwd('/home/pfs/project/cygnus-android/test/')  # Add your dir here
        # Obtain structure of the remote directory 
	directory_structure = sftp.listdir_attr()

	localFilePath = (full_path) # The path where your file is stored on your drive
	remoteFilePath = (tail) # The path where you want to upload
	sftp.put(localFilePath, remoteFilePath)

os.system("$PWD/upload.sh")
