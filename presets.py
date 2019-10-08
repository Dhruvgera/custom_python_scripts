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
print("")#I know that I can use the newline character, but yeah, I prefer this style of coding :)

q=input("Select device: \n 1. santoni \n 2. falcon \n 3. beryllium \n 4. demn  ")

#Largest file finder code
try:
    chex2=open("largest.py")
    chex2.close()
except:
    codefs='''import os, glob
largest = sorted( (os.path.getsize(s), s) for s in glob.glob('out/target/product/q/*.zip') )[-1][1]
os.environ["largest"] = largest
os.system("gdrive upload $largest")
import subprocess
import select
cmd = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
command = "gdrive upload --share $largest"
cmd.stdin.write(command)
cmd.stdin.flush() # Must include this to ensure data is passed to child process
if ready:
   result = cmd.stdout.readline()
   os.environ["link"]= result'''
    saveFile2=open("largest.py",'w')
    saveFile2.write(str(codefs))
    saveFile2.close()
    rep = open("largest.py").read()
    rep = rep.replace('q',q)
    with open('largest.py', 'w') as file:
        file.write(rep)



try: 
	checko=open("sendlink.sh")
	checko.close()
except:
	sendcode='''#!/bin/bASH
function tg_SendMsg() {
curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage  -d "parse_mode=markdown" -d text="$1 " -d chat_id=$CHAT_ID}
tg_SendMsg "$link Enjoy your freshly cooked ROM!!!!"'''
	se=open("sendlink.sh",'w')
	se.write(str(sendcode))
	se.close()

try: 
    chexlast=open("start.sh")
    chexlast.close()
except:
    buildcode='''#!/bin/bash
. b*/e*
lunch cerberus_q-userdebug
make cerberus -j$(nproc --all)'''
    saves=open("start.sh",'w')
    saves.write(str(buildcode))
    saves.close()
    fixx = open("start.sh").read()
    fixx = fixx.replace('q',q)
    with open("start.sh",'w') as file:
        file.write(fixx)

process = subprocess.Popen('start.sh', shell=True, stdout=subprocess.PIPE)  
process.wait()
e.system("python3 largest.py")
e.system("sendlink.sh")	
