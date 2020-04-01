# Copyright (C)  Dhruv Gera
echo -e "AUTOMATER by Dhruv Gera";
export BOT_API_KEY=""
export CHAT_ID=""
export SF_USR=""
export SF_PASS=""
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
cd $HOME/cygnus/
function globexists {
   test -e "$1" -o -L "$1"
}
if ! globexists Cygnus* ; then                          
   echo -e "Build failed :p";
   function SendMsg() {  
   curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage -d "parse_mode=markdown" -d text="$1" -d chat_id=$CHAT_ID 1> /dev/null 
   }
   SendMsg "Build has failed! Check the logs please";
   grep -iE 'crash|error|fail|fatal' "log.txt" &> "trimmed.txt"
   curl -F chat_id="$CHAT_ID" -F document=@"trimmed.txt" -F caption="Woah, I trimmed them for you" https://api.telegram.org/bot$BOT_API_KEY/sendDocument
   cd $HOME/cygnus/scripts/CI/
else
   python3 $HOME/cygnus/rom.py
   wait
   python3 $HOME/cygnus/tgt.py
   wait
fi
sed -i "s/$devicename/device_name_here/g" $HOME/cygnus/replacer.py
sed -i "s/$devicename/sampledevice/g" $HOME/cygnus/start.sh
sed -i "s/$devicename/sampledevice/g" $HOME/cygnus/rom.py
sed -i "s/$devicename/sampledevice/g" $HOME/cygnus/tgt.py
cd $HOME/cygnus
make clean 
rm log.txt
rm *md5sum
