#!/bin/bash
# Copyright (C)  Dhruv Gera
function transfer {
    zipname="$(echo $1 | awk -F '/' '{print $NF}')";
    url="$(curl -# -T $1 http://transfer.sh -H "Max-Downloads: 1")";
    printf '\n';
    echo -e "Download ${zipname} at ${url}";
    curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage -d text="Download build at: $url" -d chat_id=$CHAT_ID
}
function bashupload {
    zipname="$(echo $1 | awk -F '/' '{print $NF}')";
    url="$(curl -# -T $1 https://bashupload.com)";
    printf '\n';
    echo -e "Download ${zipname} at this alternative URL: ${url}";
    curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage -d text="Download build at this alternative URL: $url" -d chat_id=$CHAT_ID
}
transfer $largest
# bashupload $largest
