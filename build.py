import os as e 
import time
import glob
import subprocess
import select

#cmd = subprocess.Popen(['bash'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)


print("ROM Builder script by: ")
print(" ______   __   __  ______    __   __  __   __    _______  _______  ______    _______ ")
print("|      | |  | |  ||    _ |  |  | |  ||  | |  |  |       ||       ||    _ |  |   _   |")
print("|  _    ||  |_|  ||   | ||  |  | |  ||  |_|  |  |    ___||    ___||   | ||  |  |_|  |")
print("| | |   ||       ||   |_||_ |  |_|  ||       |  |   | __ |   |___ |   |_||_ |       |")
print("| |_|   ||       ||    __  ||       ||       |  |   ||  ||    ___||    __  ||       |")
print("|       ||   _   ||   |  | ||       | |     |   |   |_| ||   |___ |   |  | ||   _   |")
print("|______| |__| |__||___|  |_||_______|  |___|    |_______||_______||___|  |_||__| |__|")
print("")#I know that I can use the newline character, but yeah, I prefer this style of coding :)

q=input("Select device: \n 1. Santoni \n 2. To be filled \n ")

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
command = "gdrive upload $largest"
cmd.stdin.write(command)
cmd.stdin.flush() # Must include this to ensure data is passed to child process
if ready:
   result = cmd.stdout.readline()
   os.environ["link"]= result
function tg_SendMsg() {
curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage  -d "parse_mode=markdown" -d text="$1 " -d chat_id=$CHAT_ID}
tg_SendMsg "$link Enjoy your freshly cooked ROM!!!!"'''
    saveFile2=open("largest.py",'w')
    saveFile2.write(str(codefs))
    saveFile2.close()
    rep = open("largest.py").read()
    rep = rep.replace('q',q)
    with open('largest.py', 'w') as file:
        file.write(rep)
  
try: 
    chexlast=pen("start.sh")
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
'''try:
    chex3=open("upload.sh")
    chex3.close()
except:
    usr=input("Enter your sourceforge username: ")
    codeup='sftp usr@frs.sourceforge.net'
    saveFile3=open("upload.sh",'w')
    saveFile3.write(str(codeup))
    saveFile3.close()
    zz = open("upload.sh").read()
    zz.replace("usr",usr)
'''
#SF uploader code
'''try:
    check=open("sf.sh")
    check.close
except:
    writeme3=''spawn ./upload.sh
    expect "Are you sure you want to continue connecting (yes/no)?\r"
    send -- "yes\r"
    expect "Password:\r"
    send -- "pswd\r"
    expect "sftp>\r"
    send -- "put largest"
    function tg_SendMsg() {
    curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage  -d "parse_mode=markdown" -d text="$1 " -d chat_id=$CHAT_ID}
    tg_SendMsg "Zip upload done!!!"''#Create largest.py to find out the largest file in a folder(Done, useless coment)
    pswd=input("Enter your sourceforge password: ")
    saveFile=open("sf.sh",'w')#Create upload.sh to start all this chain reaction
    saveFile.write(str(writeme3))
    saveFile.close()#Shift all this code to beginning as this will be used for every device
    z = open("sf.sh").read()
    z.replace("pswd",pswd)
'''


print("Checking dependencies now!!!")

if (q=="Santoni" or "santoni"):
    try:
     e.system("cd device/xiaomi/santoni")
    except:
     print("Device tree absent! Are you drunk? Cloning now!!")
     e.system("git clone https://github.com/Dhruvgera/device_xiaomi_santoni.git device/xiaomi/santoni")
 
    try:
     check=open("vendor/xiaomi/santoni/santoni-vendor.mk")
     check.close()
    except:
     print("Vendor tree absent! Go wash your face, you noob! Cloning now!!")
     e.system("git clone https://github.com/Dhruvgera/vendor_santoni.git vendor/xiaomi")
 
    try:
     e.system("cd kernel/xiaomi/msm8937")
    except:
     print("Kernel tree absent! You pathetic person? Cloning now!!")
     e.system("git clone https://github.com/Dhruvgera/RockstarKernel_r4x.git kernel/xiaomi/msm8937")
 
    print("All dependencies are there!")
    print("Building rom now!!!")
    e.system("export USE_CCACHE=1")
    e.system("prebuilts/misc/linux-x86/ccache/ccache -M 100G")
    e.system("export CCACHE_COMPRESS=1")
    '''command = "bash build/envsetup.sh && "
    command = bytes(command, 'utf-8')
    cmd.stdin.write(command)
    cmd.stdin.flush() # Must include this to ensure data is passed to child process
    command = "lunch cerberus_santoni-userdebug"
    command = str.encode(command)
    cmd.stdin.write(command)
    cmd.stdin.flush()
    command = "make cerberus -j$(nproc --all)"
    command= str.encode(command)
    cmd.stdin.write(command)
    cmd.stdin.flush()'''
    saves=open("start.sh",'w')
    saves.write(str(buildcode))
    saves.close()
    fixx = open("start.sh").read()
    fixx = fixx.replace('q',q)
    with open("start.sh",'w') as file:
        file.write(fixx)
 #   e.system("./start.sh")
 #   subprocess.call(['. b*/e* && lunch cerberus_santoni-userdebug && make cerberus -j$(nproc --all)'])
#    subprocess.call(['./start.sh'])
    process = subprocess.Popen('start.sh', shell=True, stdout=subprocess.PIPE)  
    process.wait()
    e.system("python3 largest.py")

