# Copyright (C)  Dhruv Gera
export ZIPNAME="log.txt"
export CHAT_ID=""
export BOT_API_KEY=""
x=$(curl https://bashupload.com/$largest --data-binary @$largest)
echo "$x" 
curl -F chat_id="$CHAT_ID" -F document=@"$ZIPNAME" -F caption="$x" https://api.telegram.org/bot$BOT_API_KEY/sendDocument
