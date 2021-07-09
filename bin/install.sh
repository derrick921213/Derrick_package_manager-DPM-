#!/bin/bash
#__author__:derrick921213
py=$(python3 -c "import os" >/dev/null)

if [ "$?" != '0' ]; then
    echo "Python not install"
    exit 1
fi
is_install=$(python3 -c "import pyinstaller" >/dev/null)
if [ "$?" != "0" ]; then
    pip3 install pyinstaller >/dev/null
    if [ "$?" != '0' ]; then
        echo "Pip3 Error"
        exit 1
    fi
fi
curl -O https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/dpm.py
pyinstaller -F dpm.py
sudo mv dist/dpm /usr/local/bin
