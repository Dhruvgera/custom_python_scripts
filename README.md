# python_custom_scripts
Python scripts written by me to automate ROM compilation and upload them. Will be adding more scripts for choosing which kernel to install while flashing ROMs soon!  

# CI:
Split of up some code, perfectly working. Export your device name as export devicename="your beloved phone's codename", add your CHAT_ID and BOT_API_KEY in upload.sh and run main.sh. The programs will
run in coordination and build the ROM, upload the target files and rom zip(Add the respective zip path, cygnus generates it in the ROM dir only) to bashupload and send the resulting build log and zip to you. This setup can be used along with Jenkins to provide a seamless experience to maintainers.


# production.py:
A program to build for many devices in 1 go and ensure dependencies and send builds via Telegram bot API and other features. 

# sftp.py:
A python program to find the largest file in your requested directory and automatic uploads to sftp clients such as sourceforge. 
To make it work, ensure that pysftp is installed by running pip3 install pysftp

# incremental.py
A program to generate incremental zips automatically for ROM updates. 
