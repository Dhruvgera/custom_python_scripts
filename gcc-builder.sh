cd $HOME
mkdir gcc-builds
cd gcc-builds
git clone https://github.com/Dhruvgera/EvaGCC-arm64 gcc-arm64
rm -rf gcc-arm64/*
git clone https://github.com/mvaisakh/gcc-build.git
cd gcc-build
./build-gcc.sh -a arm64
cd ../gcc-arm64
bash $HOME/gcc-builds/gcc-build/strip-binaries.sh
git add . -f
thetime="$(date +%s)";
git commit -m "Update GCC to latest revision at ${thetime}"
git push git@github.com:Dhruvgera/EvaGCC-arm64.git HEAD:master
cd ..
git clone https://github.com/Dhruvgera/EvaGCC-arm gcc-arm
rm -rf gcc-arm/* gcc-arm64 gcc-build
git clone https://github.com/mvaisakh/gcc-build.git
cd gcc-build
./build-gcc.sh -a arm
cd ../gcc-arm
bash $HOME/gcc-builds/gcc-build/strip-binaries.sh
git add . -f
thetime="$(date +%s)";
git commit -m "Update GCC ARM to latest revision at ${thetime}"
git push git@github.com:Dhruvgera/EvaGCC-arm.git HEAD:master
cd $HOME
rm -rf gcc-builds
