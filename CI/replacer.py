# Copyright (C)  Dhruv Gera
import os
import time
import glob
import subprocess
import select
devicename="device_name_here"
fin = open("uploader.py", "rt")
data = fin.read()
data = data.replace('q', devicename)
fin.close()

fin = open("uploader.py", "wt")
fin.write(data)
fin.close()


fin = open("start.sh", "rt")
data = fin.read()
data = data.replace('q', devicename)
fin.close()

fin = open("start.sh", "wt")
fin.write(data)
fin.close()

