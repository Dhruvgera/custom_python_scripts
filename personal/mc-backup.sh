#!/bin/bash

# This script assumes that the minecraft world is in the root dir
mkdir backups
cp -r world* backups/
cd backups

# Nuke git everytime so we don't hit the repo file size limit
sudo rm -rf .git
git init

# Zip all the world folders into a file
zip -r backup.zip *
git add backup.zip
git commit -m "New Backup"

# Force push the file
git push -f git@gitlab.com:Dhruvgera/mc-backups.git HEAD:main
cd $HOME

# Clean up what you did
rm -rf backups
