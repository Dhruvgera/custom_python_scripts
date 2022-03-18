# Import basic modules
import os,sys

# Pass the name of the file
filename=sys.argv[1]

# Split the filename to get the devicename, we are using the 4th element aka 3rd index
devicename=filename.split('-')
devicename=devicename[3]

# Declare a device list
device_list=["beryllium","G","lavender","ginkgo","violet","r5x"]

# Upload the actual build to your FTP
for i in device_list:
    if i == devicename:
        os.environ["devicename"] = i
        os.environ["filename"] = filename
        os.system("ftp-upload -h IP -u USERNAME --password YOUR_PASS -d $devicename/ $filename")
    else:
        pass
