#!/bin/bash
export PATH="~/.local/bin:$PATH"
curl -H "Cache-Control: no-cache" -O https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/dpm.py
pyinstaller -F dpm.py
sudo rm -rf /usr/local/bin/dpm
sudo mv dist/dpm /usr/local/bin
sudo rm -rf __pycache__ dist build dpm.spec dpm.py