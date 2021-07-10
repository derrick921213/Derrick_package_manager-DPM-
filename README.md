# Derrick Package Manager (DPM)

## Introduction

DPM is a software manager, full name is Derrick Package Manager.  
DPM can install on **Linux or Mac**, so only need to remember one command.

## Install

### Requirement

- Ubuntu/Debain: **sudo apt install python3-pip**
- CentOS/Red hat:**sudo yum|dnf install python3-pip**  
  `sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/bin/install.sh)"`

## Uninstall

`sudo /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/bin/uninstall.sh)"`

## Useage

- **sudo dpm install \<package\>** Install package
- **sudo dpm uninstall \<package\>** Uninstall package
- **sudo dpm search \<package\>** Search package from my repository
- **sudo dpm search list** Show all package in my repository
- **sudo dpm list** Show installed package (Only show install from my repository)
- **sudo dpm help** Show help page
