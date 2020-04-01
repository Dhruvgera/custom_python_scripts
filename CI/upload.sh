# Copyright (C)  Dhruv Gera
export ZIPNAME="log.txt"
curl -F chat_id="$CHAT_ID" -F document=@"$ZIPNAME" -F caption="Download build at: https://sourceforge.net/projects/cygnus-android/files/test/$largest/download" https://api.telegram.org/bot$BOT_API_KEY/sendDocument
