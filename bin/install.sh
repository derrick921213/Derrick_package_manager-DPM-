#!/bin/bash
#__author__:derrick921213
export PATH="~/.local/bin:$PATH"
py=$(python3 -c "import os" >/dev/null)

if [ "$?" != '0' ]; then
    echo "Python not install"
    exit 1
fi
is_install=$(python3 -c "import pyinstaller")
if [ "$?" != "0" ]; then
    pip3 install pyinstaller requests >/dev/null
    if [ "$?" != '0' ]; then
        echo "Pip3 Error"
        exit 1
    fi
fi
curl -H "Cache-Control: no-cache" -O https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/dpm.py
pyinstaller -F dpm.py >/dev/null
if [ "$?" != "0" ]; then
    echo "Install Error!!"
    exit 1
fi
echo [DPM] Install successful.
sudo mv dist/dpm /usr/local/bin
sudo rm -rf __pycache__ dist build dpm.spec dpm.py
