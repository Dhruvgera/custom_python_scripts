git config --global user.email dhruvgera61@gmail.com 
git config --global user.name dhruv 
git clone https://github.com/akhilnarang/scripts 
cd scripts 
bash setup/android_build_env.sh 
mkdir -p ~/bin 
cd
git clone https://android.googlesource.com/tools/repo bin/repo
printf '\n' | tee -a ~/.bashrc
sudo apt-get install cpufrequtils
echo "sudo cpufreq-set -r -g performance" >> .bashrc
echo 'deb http://deb.xanmod.org releases main' | sudo tee /etc/apt/sources.list.d/xanmod-kernel.list && wget -qO - https://dl.xanmod.org/gpg.key | sudo apt-key add -
sudo apt update && sudo apt install linux-xanmod
sudo reboot
ccache -M 100G
