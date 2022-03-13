# Copyright (C) 2020 Dhruv Gera
import subprocess
import select
import os
import sys
import glob

# Device name is here for rom builds, as we need it in the out folder's name
devicename="sampledevice"

# Largest file finder
objects = os.listdir(".") # Replace with the dir you want to search in

sofar = 0
name = ""

for item in objects:
        size = os.path.getsize(item) 
        if size > sofar:
                sofar = size
                name = item
os.environ["largest"] = name
os.system("$PWD/upload.sh")
os.system("rm $largest")
