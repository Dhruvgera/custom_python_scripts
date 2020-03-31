# Copyright (C)  Dhruv Gera
import os
import time
import glob
import subprocess
import select
devicename="device_name_here"

fin = open("start.sh", "rt")
data = fin.read()
data = data.replace('sampledevice', devicename)
fin.close()

fin = open("start.sh", "wt")
fin.write(data)
fin.close()

