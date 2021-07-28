import os
repo_list=["build_soong","vendor_cygnus","vendor_qcom_opensource_data-ipa-cfg-mgr","vendor_qcom_opensource_commonsys_cryptfs_hw","vendor_qcom_opensource_interfaces","vendor_qcom_opensource_dataservices","vendor_qcom_opensource_recovery-ext","vendor_qcom_opensource_vibrator","frameworks_native","frameworks_base","frameworks_opt_telephony","frameworks_opt_net_ims","bootable_recovery","packages_apps_Settings","packages_providers_TelephonyProviders","packages_services_Telephony","device_qcom_sepolicy","system_core","system_vold","system_sepolicy","hardware_qcom_wlan","platform_testing","external_fastrpc","external_tinycompress","hardware_libhardware"]
for i in repo_list:
	j=i.replace("_","/",4)
	os.system("cd "+j+" && git push https://github.com/cygnus-rom/"+i+" HEAD:caf-11")
