# Copyright (C)  Dhruv Gera
export ZIPNAME="log.txt"
export CHAT_ID=""
export BOT_API_KEY=""
curl -F chat_id="$CHAT_ID" -F document=@"$ZIPNAME" -F caption="Download build at: https://sourceforge.net/projects/cygnus-android/files/test/$largest/download" https://api.telegram.org/bot$BOT_API_KEY/sendDocument
