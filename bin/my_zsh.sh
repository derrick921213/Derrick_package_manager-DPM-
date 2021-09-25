#!/bin/bash
#Author Derrick
echo ""
echo "#############################################################"
echo "# Automatically to  Install oh-my-zsh and initialize it     #"
echo "# Author: Derrick<dlin12457.work@gmail.com>                 #"
echo "#############################################################"
echo ""

function checkOS(){
    if [ -f /etc/redhat-release ]
    then
        OS="CentOS"
    elif [ ! -z "`cat /etc/issue | grep -i bian`" ]
    then
        OS="Debian"
    elif [ ! -z "`cat /etc/issue | grep -i ubuntu`" ]
    then
        OS="Ubuntu"
    else
        echo "Not supported OS"
        exit 1
    fi
}

function installSoftware(){
    if [ "$OS" == 'CentOS' ]
        then
	        sudo yum -y install zsh git vim > /dev/null
        else
	        sudo apt-get -y install zsh git vim > /dev/null
    fi
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
}

function Download(){
    curl -O  https://mcserver.tplinkdns.com/file/.zshrc
    curl -O  https://mcserver.tplinkdns.com/file/.vimrc
    mv .zshrc .vimrc ~
    source ~/zshrc
}

function config(){
    mkdir ~/.zplug
    export ZPLUG_HOME=~/.zplug
    git clone https://github.com/zplug/zplug $ZPLUG_HOME
}
function main(){
    Download
    checkOS
    installSoftware
    config
}
main
