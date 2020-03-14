#!/bin/bash
# Copyright (C)  Dhruv Gera
export CHAT_ID=""
export BOT_API_KEY=""
export USE_NINJA=true
export USE_CCACHE=1
export CCACHE_EXEC=$(command -v ccache)
export CCACHE_BASEDIR="$HOME/.ccache"
. b*/e*
lunch cygnus_q-userdebug
curl -F chat_id=$CHAT_ID  -F text="Build scheduled for q started" https://api.telegram.org/bot$BOT_API_KEY/sendMessage
mka cygnus | tee log.txt

