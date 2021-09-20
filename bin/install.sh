#!/bin/bash
#__author__:derrick921213
export PATH="~/.local/bin:$PATH"
py=$(python3 -c "import os" >/dev/null)

if [ "$?" != '0' ]; then
    echo "Python not install"
    exit 1
fi
is_install=$(python3 -c "import pyinstaller" && python3 -c "import requests" && python3 -c "import argcomplete")
if [ "$?" != "0" ]; then
    sudo pip3 install pyinstaller requests argcomplete pyzshcomplete >/dev/null 2>&1
    sudo activate-global-python-argcomplete
    activate_pyzshcomplete
    if [ "$?" != '0' ]; then
        echo "Pip3 Error"
        exit 1
    fi
fi
curl -H "Cache-Control: no-cache" -o dpm.py https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/dpm.py?$(date +%s)
pyinstaller -F dpm.py >/dev/null 2>&1
if [ "$?" != "0" ]; then
    echo "Install Error!!"
    exit 1
fi
sudo mv dist/dpm /usr/local/bin
sudo rm -rf __pycache__ dist build dpm.spec dpm.py
echo [DPM] Install successful.
echo "If your shell is zsh, add "
echo 'eval "$(~/.local/bin/register-python-argcomplete dpm)"'
echo 'in ~/.zshrc'
