# Derrick Package Manager (DPM)

## 介紹

DPM 是一個軟體套件管理程式, 全名叫 Derrick Package Manager.  
DPM 可以安裝在 **Linux or Mac**, 所以只需要記得一種指令

## 安裝

### 需求

- Ubuntu/Debain: **sudo apt install python3-pip curl**
- CentOS/Red hat:**sudo yum|dnf install python3-pip curl**

### 執行下面指令即可安裝 DPM

`/bin/bash -c "$(curl -fsSL -H "Cache-Control: no-cache" https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/bin/install.sh)"`

## 解除安裝

`/bin/bash -c "$(curl -fsSL -H "Cache-Control: no-cache" https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/bin/uninstall.sh)"`

## 使用方法

- **dpm install \<package\>** 安裝軟體包
- **dpm uninstall \<package\>** 移除軟體包
- **dpm search \<package\>** 從我的倉儲搜尋軟體包
- **dpm search list** 列出我倉儲可提供的軟體包
- **dpm list** 列出已安裝程式 (只列出我倉儲內以安裝的程式)
- **dpm help** 顯示幫助頁面
- **dpm update** 更新已安裝的程式
