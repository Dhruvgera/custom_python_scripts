import os,sys
a = sys.argv[1]
os.environ['a'] = a
os.system("wget $a")
a=a.split('/')
a=a[-1]
os.environ['filename'] = a
os.system("python3 release.py $filename")
