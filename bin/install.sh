#!/bin/bash
#__author__:derrick921213
export PATH="~/.local/bin:$PATH"
py=$(python3 -c "import os" >/dev/null)

if [ "$?" != '0' ]; then
    echo "Python not install"
    exit 1
fi
pip3 install --user pyinstaller requests argcomplete pyzshcomplete
activate-global-python-argcomplete
activate_pyzshcomplete
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
echo 'autoload -U bashcompinit;bashcompinit'
echo 'AND'
echo 'eval "$(~/.local/bin/register-python-argcomplete dpm)"'
echo 'in ~/.zshrc'
