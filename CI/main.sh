# Copyright (C)  Dhruv Gera
mv $PWD/scripts/CI/upload.sh $HOME/cygnus/
mv $PWD/scripts/CI/replacer.py $HOME/cygnus/
mv $PWD/scripts/CI/start.sh $HOME/cygnus/
mv $PWD/scripts/CI/rom.py $HOME/cygnus/
mv $PWD/scripts/CI/tgt.py $HOME/cygnus/
sed -i "s/device_name_here/$devicename/g" $HOME/cygnus/replacer.py
sed -i "s/sampledevice/$devicename/g" $HOME/cygnus/rom.py
sed -i "s/sampledevice/$devicename/g" $HOME/cygnus/tgt.py
python3 $HOME/cygnus/replacer.py
wait
bash $HOME/cygnus/start.sh
wait
python3 $HOME/cygnus/rom.py
wait
python3 $HOME/cygnus/tgt.py
wait
sed -i "s/$devicename/device_name_here/g" $HOME/cygnus/replacer.py
sed -i "s/$devicename/q/g" $HOME/cygnus/start.sh
sed -i "s/$devicename/sampledevice/g" $HOME/cygnus/rom.py
sed -i "s/$devicename/sampledevice/g" $HOME/cygnus/tgt.py
cd $HOME/cygnus
make clean 
rm -rf log.txt
