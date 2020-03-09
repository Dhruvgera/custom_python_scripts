#!/bin/bash
# Copyright (C)  Dhruv Gera
export USE_NINJA=true
export USE_CCACHE=1
export CCACHE_EXEC=$(command -v ccache)
export CCACHE_BASEDIR="$HOME/.ccache"
. b*/e*
lunch cygnus_q-userdebug
mka cygnus

