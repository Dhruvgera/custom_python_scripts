# Copyright (C)  Dhruv Gera
mv $PWD/scripts/CI/upload.sh $HOME/cygnus/
mv $PWD/scripts/CI/replacer.py $HOME/cygnus/
mv $PWD/scripts/CI/uploader.py $HOME/cygnus/
mv $PWD/scripts/CI/start.sh $HOME/cygnus/
sed -i "s/device_name_here/$devicename/g" $HOME/cygnus/replacer.py
python3 $HOME/cygnus/replacer.py
wait
bash $HOME/cygnus/start.sh
wait
python3 $HOME/cygnus/uploader.py
wait
sed -i "s/$devicename/device_name_here/g" $HOME/cygnus/replacer.py
sed -i "s/$devicename/q/g" $HOME/cygnus/start.sh
sed -i "s/$devicename/q/g" $HOME/cygnus/uploader.py
cd $HOME/cygnus
make clean 
