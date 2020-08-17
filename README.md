# python_custom_scripts
Python scripts written by me to automate ROM compilation and upload them. Will be adding more scripts for choosing which kernel to install while flashing ROMs soon!  

# CI (AUTOMATER):
A combination of various programs, with the addition of few variables like CHAT_ID etc. , this can do:

- Trigger the build of your ROM
- Send message about the build status
- Upload the build and target files to any SFTP client
- Send you the direct download links 
- Send the build log
- If the build fails, abort other statements, and send you trimmed build logs
- Clean everything and restore the server to the previous state
- Can be integrated with Jenkins to provide 1 click builds
- Some other miscellanous functionality


# production.py :
[Broken and depreceated, please use CI (Automater)] 
A program to build for many devices in 1 go and ensure dependencies and send builds via Telegram bot API and other features. 

# sftp.py :
A python program to find the largest file in your requested directory and automatic uploads to sftp clients such as sourceforge. 
To make it work, ensure that pysftp is installed by running pip3 install pysftp

# incremental.py :
A program to generate incremental zips automatically for ROM updates. 

# linux-android-compile.sh :

Yeah, I know it's bash. A simple program which does the following stuff:

- Send the build and stats to Telegram in a nice way
- Upload build logs and trim them if the Build fails
- Inform about build starting, the last commit etc.
- Zipping the compiled image 
- Make your life a lot easier by taking care of all build steps
- Cleans up the directory afterwards
- Also can upload builds to transfer.sh, if you want it to
- Some other miscellaneous stuff
