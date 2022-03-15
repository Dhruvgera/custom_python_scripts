#!/bin/bash

# This script assumes that the minecraft world is in the root dir
mkdir backups
cp -r world* backups/
cd backups

# Nuke git everytime so we don't hit the repo file size limit
sudo rm -rf .git
git init

# Add a README files
echo "Backups for minecraftbutcursed.com world" > README.md

# Zip all the world folders into a file
zip -r backup.zip *

# Do Git LFS thingies
git lfs install
git lfs track backup.zip
git add .gitattributes
git add README.md
git add backup.zip
git commit -m "New Backup"

# Force push the file
git push -f git@github.com:Dhruvgera/mc-backups.git HEAD:main
cd $HOME

# Clean up what you did
rm -rf backups
