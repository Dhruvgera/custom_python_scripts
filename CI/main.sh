# Copyright (C)  Dhruv Gera
mv upload.sh $HOME/cygnus/
mv replacer.py $HOME/cygnus/
mv uploader.py $HOME/cygnus/
mv start.sh $HOME/cygnus/
sed -i "s/device_name_here/$devicename/g" $HOME/cygnus/replacer.py
python3 $HOME/cygnus/replacer.py
bash $HOME/cygnus/start.sh
python3 $HOME/cygnus/uploader.py
sed -i "s/$devicename/device_name_here/g" $HOME/cygnus/replacer.py
sed -i "s/$devicename/q/g" $HOME/cygnus/start.sh
sed -i "s/$devicename/q/g" $HOME/cygnus/uploader.py
cd $HOME/cygnus
make clean 
