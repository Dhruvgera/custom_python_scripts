# Copyright (C)  Dhruv Gera
mv $PWD/scripts/upload.sh $HOME/cygnus/
mv $PWD/scripts/replacer.py $HOME/cygnus/
mv $PWD/scripts/uploader.py $HOME/cygnus/
mv $PWD/scripts/start.sh $HOME/cygnus/
sed -i "s/device_name_here/$devicename/g" replacer.py
python3 $HOME/cygnus/replacer.py
bash $HOME/cygnus/start.sh
python3 uploader.py
sed -i "s/$devicename/device_name_here/g" replacer.py

