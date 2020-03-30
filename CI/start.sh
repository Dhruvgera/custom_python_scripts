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
curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage -d text="Build Scheduled for q started" -d chat_id=$CHAT_ID
mka cygnus | tee log.txt

