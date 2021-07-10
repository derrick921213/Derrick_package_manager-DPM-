# Derrick Package Manager (DPM)

## Introduction

DPM is a software manager, full name is Derrick Package Manager.  
DPM can install on **Linux or Mac**, so only need to remember one command.

## Install

### Requirement

- Ubuntu/Debain: **sudo apt install python3-pip curl**
- CentOS/Red hat:**sudo yum|dnf install python3-pip curl**

### Run below command to install DPM

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/bin/install.sh)"`

## Uninstall

`/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/bin/uninstall.sh)"`

## Useage

- **dpm install \<package\>** Install package
- **dpm uninstall \<package\>** Uninstall package
- **dpm search \<package\>** Search package from my repository
- **dpm search list** Show all package in my repository
- **dpm list** Show installed package (Only show install from my repository)
- **dpm help** Show help page
