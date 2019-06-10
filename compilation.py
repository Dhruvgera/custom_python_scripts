//ROM compilation python programme
import subprocesses as e

//File Checker
def FE(fileNameStr):
return path.exists(fileNameStr)

K = "Dependency exists"
KN = "A dependency doesn't exist, cloning"

e.call("function tg_SendMsg() {	curl -s -X POST https://api.telegram.org/bot$BOT_API_KEY/sendMessage -d "parse_mode=markdown" -d text="$1 " -d chat_id=$CHAT_ID}")

print ("Select the device: ")
v = input("1. Santoni") 
print(v)
if (v == 1 or Santoni):
  print("Checking dependencies")
  FE("kernel/xiaomi/msm8937/arch/arm64/           configs/santoni_treble-defconfig");
  if (FE == true):
    print(K)
  else
    print(KN)
    e.call("git clone https://github.com/Dhruvgera/RockstarKernel-r4x -b rom-non_oc kernel/xiaomi/msm8937")
    FE("device/xiaomi/santoni/cerberus_santoni.mk");
  if (FE == true):
    print(K)
  else
    print(KN)
    e.call("git clone https://github.com/Dhruvgera/device_xiaomi_santoni device/xiaomi/santoni")
    FE("vendor/xiaomi/santoni");
  if (FE == true):
    print(K)
  else
    print(KN)
    e.call("")    
    print("Building ROM now!")
    e.call("export USE_CCACHE=1")
    e.call("prebuilts/misc/linux-x86/ccache/ccache -M 100G")
    e.call("export CCACHE_COMPRESS=1")
    e.call(". b*/e*")
    e.call("lunch cerberus_santoni-userdebug")
    e.call("mka cerberus")


//Upload ROM to tg

e.call("function tg_SendDoc() {	curl -F chat_id=$CHAT_ID -F document=@"$1" -F caption="$2" https://api.telegram.org/bot$BOT_API_KEY/sendDocument}")

e.call("export $CHAT_ID=")
e.call("export $BOT_API_KEY=")

e.call("$FINAL_ZIP=$HOME/cerberus/out/target/product/santoni/Cerberus*")
e.call("tg_SendDoc "$FINAL_ZIP"")
else:
e.call("tg_SendMsg "Zip Creation Failed "")
