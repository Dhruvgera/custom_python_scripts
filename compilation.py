#ROM compilation personalised python prgramme maker
import os as e 
import time
rom_name=input("Enter ROM name (In lowercase): ")
print(rom_name)
device_name=input("Enter device name (In lowercase): ")
print(device_name)
oem_name=input("Enter device manufacturer's name (In lowercase): ")
print(oem_name)
device_kernel_name=input("Enter your device chipset's codename: ")
print(device_kernel_name)
vt_link=input("Enter your vendor tree link: ")
print(vt_link)
kt_link=input("Enter your kernel tree link: ")
print(kt_link)
dt_link=input("Enter your device tree link: ")
print(dt_link)




#Main compilation script
writeme='''import os as e
print("Checking dependencies...")
try:
 check=open("device/oem2_name/device2_name'/rom2_name_device2_name.mk'")
 check.close()
except:
 print("Device tree absent! Are you drunk? Cloning now!!")
 e.system("git clone dt2_link")
 
try:
 check=open("vendor/oem2_name/device2_name/device2_name-vendor.mk")
 check.close()
except:
 print("Vendor tree absent! Go wash your face, you noob! Cloning now!!")
 e.system("git clone vt2_link")
 
try:
 check=open("kernel/oem2_name/device2_kernel_name/device2_name_defconfig")
 check.close()
except:
 print("Kernel tree absent! You pathetic person? Cloning now!!")
 e.system("git clone kt2_link")
 
print("All dependencies are done!")

#Begin ROM compilation

print("Building ROM now!")
e.system("export USE_CCACHE=1")
e.system("prebuilts/misc/linux-x86/ccache/ccache -M 100G")
e.system("export CCACHE_COMPRESS=1")
e.system(". b*/e*")
e.system("'lunch rom2_name_device2_name-userdebug")
e.system("make -j$(nproc --all)")

try:
 romchex=open("'out/target/product/'+'device2_name'.strip()+'/'+'rom2_name'.strip()+'*'")
 romchex.close()
 e.system("bash uploader.sh")
except:
 try:
  time.sleep(3600)
  romchex=open("'out/target/product/'+'device2_name'.strip()+'/'+'rom2_name'.strip()+'*'")
  romchex.close()
  e.system("bash uploader.sh")
 except:
   try:
    time.sleep(3600)
    romchex=open("'out/target/product/'+'device2_name'.strip()+'/'+'rom2_name'.strip()+'*'")
    romchex.close()
    e.system("bash uploader.sh")
   except:
      try:
       time.sleep(3600)
       romchex=open("'out/target/product/'+'device2_name'.strip()+'/'+'rom2_name'.strip()+'*'")
       romchex.close()
       e.system("bash uploader.sh")
      except:
        try:
         time.sleep(3600)
         romchex=open("'out/target/product/'+'device2_name'.strip()+'/'+'rom2_name'.strip()+'*'")
         romchex.close()
         e.system("bash uploader.sh")
        except:
           try:
            time.sleep(3600)
            romchex=open("'out/target/product/'+'device2_name'.strip()+'/'+'rom2_name'.strip()+'*'")
            romchex.close()
            e.system("bash uploader.sh")
           except:
            try:
             time.sleep(3600)
             romchex=open("'out/target/product/'+'device2_name'.strip()+'/'+'rom2_name'.strip()+'*'")
             romchex.close()
             e.system("bash uploader.sh")
            except:
             try:
              time.sleep(3600)
              romchex=open("'out/target/product/'+'device2_name'.strip()+'/'+'rom2_name'.strip()+'*'")
              romchex.close()
              e.system("bash uploader.sh")
             except:
              print(GO DIE YOU NOOB")'''


#writeme2="function transfer() {
 #   zipname="$(echo $1 | awk -F '/' '{print $NF}')";
  #  url="$(curl -# -T $1 https://transfer.sh)";
   # printf '\n';
   # echo -e "Download ${zipname} at ${url}";
   # curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage -d text="$url" -d chat_id=$CHAT_ID
   # curl -F chat_id="$CHAT_ID" -F document=@"${ZIP_DIR}/$ZIPNAME" https://api.telegram.org/bot$BOT_API_KEY/sendDocument
#}

#export ZIPDIR = "out/target/product/'+device2_name+'/'"
#export ZIPNAME = "rom2_name*";
#export BOT_API_KEY = botapikey2
#export CHAT_ID = chatid2

#transfer();"


saveFile=open(device_name.strip()+'.py'.strip(),'w')
saveFile.write(str(writeme))
saveFile.close()

'''saveFile2=open("uploader.sh","w")
saveFile2.write(str(writeme2))
saveFile2.close()'''

s = open(device_name.strip()+'.py'.strip()).read()
s = s.replace('device2_name', device_name)
s = s.replace('rom2_name',rom_name)
s = s.replace('oem2_name',oem_name)
s = s.replace('device2_kernel_name',device_name)
s = s.replace('vt2_link', vt_link)
s = s.replace('kt2_link', kt_link)
s = s.replace('dt2_link', dt_link)
f = open(device_name.strip()+'.py'.strip(), 'w')
f.write(s)
f.close()

'''s = open("uploader.sh").read()
s = s.replace('device2_name', '"'+device_name+'"')
s = s.replace('rom2_name', '"'+rom_name+'"')
s = s.replace('oem2_name', '"'+oem_name+'"')
s = s.replace('device2_kernel_name', '"'+device_name+'"')
s = s.replace('vt2_name', '"'+device_name+'"')
s = s.replace('kt2_name', '"'+device_name+'"')
s = s.replace('dt2_name', '"'+device_name+'"')
f = open("device_name'.txt'", 'w')
f.write(s)
f.close()
''' 

e.system('python3'+' '+device_name.strip()+'.py'.strip()) 
