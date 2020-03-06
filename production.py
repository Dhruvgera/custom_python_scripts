# Copyright (C) Dhruv Gera
import os as e 
import time
import glob
import subprocess
import select

print("ROM Builder script by: ")
print(" ______   __   __  ______    __   __  __   __    _______  _______  ______    _______ ")
print("|      | |  | |  ||    _ |  |  | |  ||  | |  |  |       ||       ||    _ |  |   _   |")
print("|  _    ||  |_|  ||   | ||  |  | |  ||  |_|  |  |    ___||    ___||   | ||  |  |_|  |")
print("| | |   ||       ||   |_||_ |  |_|  ||       |  |   | __ |   |___ |   |_||_ |       |")
print("| |_|   ||       ||    __  ||       ||       |  |   ||  ||    ___||    __  ||       |")
print("|       ||   _   ||   |  | ||       | |     |   |   |_| ||   |___ |   |  | ||   _   |")
print("|______| |__| |__||___|  |_||_______|  |___|    |_______||_______||___|  |_||__| |__|")
print(" ")#I know that I can use the newline character, but yeah, I prefer this style of coding :)
#Largest file finder code

listdevice=["beryllium","whyred","santoni","rosy","lavender","onclite"]

n=len(listdevice)

for i in range(0,n):
	devicename=listdevice[i]
	
	try:
		chex2=open("largest.py")
		chex2.close()
	except:
		codefs='''import os, glob
objects = os.listdir("$PWD")

sofar = 0
name = ""

for item in objects:
        size = os.path.getsize(item)
        if size > sofar:
                sofar = size
                name = "out/target/product/q/"+item

os.environ["name"] = largest
import subprocess
import select
cmd = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
os.system("bash $PWD/upload.sh")'''
		saveFile2=open("largest.py",'w')
		saveFile2.write(str(codefs))
		saveFile2.close()
	fin = open("largest.py", "rt")
	data = fin.read()
	data = data.replace('q', devicename)
	fin.close()

	fin = open("largest.py", "wt")
	fin.write(data)
	fin.close()
	try:
    		chex3=open("upload.sh")
    		chex3.close()
	except:
		uploadcode='''export ZIPNAME=$largest
                curl -F chat_id="$CHAT_ID" -F document=@"$ZIPNAME" -F caption="Build completed for device q" https://api.telegram.org/bot$BOT_API_KEY/sendDocument
                curl -F chat_id="$CHAT_ID" -F document=@"$HOME/cygnus/log.txt" -F caption="Build Log" https://api.telegram.org/bot$BOT_API_KEY/sendDocument
		make clean
                rm -rf log.txt device/* vendor/*  hardware/* commonsys*
                repo sync -j$(nproc --all) --force-sync --no-tags --no-clone-bundle --prune --optimized-fetch
                '''
		saveFile69=open("upload.sh",'w')
		saveFile69.write(str(uploadcode))
		saveFile69.close()
	fin = open("upload.sh", "rt")
	data = fin.read()
	data = data.replace('q', devicename)
	fin.close()

	fin = open("upload.sh", "wt")
	fin.write(data)
	fin.close()

	try: 
		chexlast=pen("start.sh")
		chexlast.close()
	except:
		buildcode='''#!/bin/bash
		. b*/e*
		lunch cygnus_q-userdebug
		curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage -d text="Build Scheduled for q has started" -d chat_id=$CHAT_ID
		mka cygnus | tee log.txt'''
		saves=open("start.sh",'w')
		saves.write(str(buildcode))
		saves.close()
	fixx = open("start.sh").read()
	fixx = fixx.replace('q',devicename)
	with open("start.sh",'w') as file:
		file.write(fixx)
	e.system("chmod +x $PWD/start.sh")
	e.system("chmod +x $PWD/upload.sh")
	p=subprocess.Popen(['$PWD/start.sh'], shell=True, executable="/bin/bash")
	p.wait()
	e.system("python3 largest.py")
