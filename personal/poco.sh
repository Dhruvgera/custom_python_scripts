rm -rf hardware/qcom/audio hardware/qcom/media hardware/qcom/display vendor/xiaomi vendor/asus kernel/xiaomi kernel/oneplus kernel/realme device/xiaomi device/realme device/oneplus
git clone https://github.com/Dhruvgera/device_xiaomi_beryllium.git  -b cygnus-caf device/xiaomi/beryllium 
git clone https://github.com/Dhruvgera/beryllium.git -b cygnus-caf device/xiaomi/sdm845-common 
git clone https://github.com/Dhruvgera/vendor_xiaomi_beryllium.git vendor/xiaomi -b rebase --depth=1  
git clone https://github.com/Dhruvgera/RockstarKernel_beryllium.git -b backup kernel/xiaomi/beryllium --depth=1 
git clone https://gitlab.com/ninadpatilbvp/vendor_xiaomi_beryllium_firmware vendor/xiaomi/beryllium/firmware 
git clone https://github.com/LineageOS/android_hardware_qcom_audio -b lineage-17.1-caf-sdm845 hardware/qcom/audio 
git clone https://github.com/LineageOS/android_hardware_qcom_media -b lineage-17.1-caf-sdm845 hardware/qcom/media 
git clone https://github.com/AOSPA/android_hardware_qcom_display -b quartz-845 hardware/qcom/display 
git clone https://github.com/AOSPA/android_vendor_qcom_opensource_commonsys-intf_display -b quartz-845 vendor/qcom/opensource/commonsys/display-intf
export devicename="beryllium"
bash $HOME/cygnus/scripts/main.sh
