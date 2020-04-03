cd $HOME/cygnus/
git clone https://github.com/Dhruvgera/device_xiaomi_beryllium.git  -b cygnus-caf device/xiaomi/beryllium
cd device/xiaomi/beryllium
git push -f https://github.com/Cygnus-devices/device_xiaomi_beryllium.git HEAD:caf-ten
cd ../../..
git clone https://github.com/Dhruvgera/beryllium.git -b cygnus-caf device/xiaomi/sdm845-common
cd device/xiaomi/sdm845-common
git push -f https://github.com/Cygnus-devices/device_xiaomi_sdm845-common.git HEAD:caf-ten
cd ../../..
git clone https://github.com/Dhruvgera/vendor_xiaomi_beryllium.git vendor/xiaomi -b rebase
cd vendor/xiaomi
git push -f https://github.com/Cygnus-devices/vendor_xiaomi_beryllium.git HEAD:caf-ten
cd ../..
git clone https://github.com/Dhruvgera/RockstarKernel_beryllium.git kernel/xiaomi/beryllium
cd kernel/xiaomi/beryllium
git push https://github.com/Cygnus-devices/kernel_xiaomi_beryllium.git HEAD:caf-ten
cd ../..
