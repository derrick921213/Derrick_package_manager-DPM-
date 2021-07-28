#!/bin/bash
sudo apt update -y
sudo apt upgrade -y
sudo apt install vim net-tools curl build-essential openjdk-8-jdk-headless fp-compiler postgresql postgresql-client python3.6 cppreference-doc-en-html cgroup-lite libcap-dev zip python3.6-dev libpq-dev libcups2-dev libyaml-dev libffi-dev python3-pip -y
cd ~/Downloads
wget https://github.com/cms-dev/cms/releases/download/v1.4.rc1/v1.4.rc1.tar.gz
tar -xvf v1.4.rc1.tar.gz
cd cms
echo y | sudo python3 prerequisites.py install
sudo pip3 install -r requirements.txt
sudo python3 setup.py install
read -sp "SET SQL password:" passwd
echo -e "\n"
sudo -u postgres createuser --username=postgres --pwprompt cmsuser
sudo -u postgres createdb --username=postgres --owner=cmsuser cmsdb
sudo -u postgres psql --username=postgres --dbname=cmsdb --command='ALTER SCHEMA public OWNER TO cmsuser'
sudo -u postgres psql --username=postgres --dbname=cmsdb --command='GRANT SELECT ON pg_largeobject TO cmsuser'
sudo sed -e "s/your_password_here/$passwd/" -i /usr/local/etc/cms.conf
sudo cmsInitDB
