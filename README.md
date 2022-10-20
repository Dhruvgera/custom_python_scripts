# custom_python_scripts ( bash too )
Python scripts written by me to automate ROM compilation and upload them. Also automate mundane tasks like pushing loads of repos, cron jobs, backups etc.

# CI (AUTOMATER):
A combination of various programs, with the addition of few variables like CHAT_ID etc. , this can do:

- Trigger the build of your ROM
- Send message about the build status
- Upload the build and target files to any SFTP client
- Send you the direct download links 
- Send the build log 
- Upload builds to CLI services and send links to Telegram
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

# sshtunnel.ps1 :

Yes, powershell is also here now

- Reverse ssh tunnel in background
- Forward multiple ports
- Kill older ports connection in case connection suddenly dies and remote server ports are stuck
- Make sure to enable Gatewayports and clientaliveinterval in sshd_config to prevent death on idle
- Run this on boot with Task Scheduler to automate the entire thing
