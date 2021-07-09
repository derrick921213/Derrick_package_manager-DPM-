#!/bin/bash
from sys import platform as plat
from urllib.request import urlopen
import json
import sys
import os
import requests as req
from tqdm import tqdm


def system_platform():
    if plat == 'win32':
        print('Platform_Error:This application only on Linux or Mac')
        sys.exit(1)
    return 'linux' if plat == 'linux' else 'darwin'


def linux_shell():
    pass


def mac_shell():
    pass


def default_shell():
    pass


def read_package_list(package):
    data_json = package_list()
    if package in data_json:
        print(f'[{package}] Found!!')
        return data_json[package]["url"]
    else:
        print(f'[{package}] not found!!')


def package_list():
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    url = "https://raw.githubusercontent.com/derrick921213/package_manager_server/main/package.json"
    response = urlopen(url)
    data = json.loads(response.read())
    response.close()
    return data


def download_file(url):

    filename = url.split('/')[-1]
    r = req.get(url, stream=True)
    with open("/tmp/"+filename, 'wb') as f:
        for data in tqdm(r.iter_content(1024)):
            f.write(data)
    return filename


def install(package):
    file = os.system(f"cd /tmp;ls | grep '^dpm_{package}'")
    if file == 0:
        success = os.system(
            f"temp=/tmp;a=`ls $temp | grep '^dpm_{package}'`;tar -xzvf $temp/$a -C /usr/local/bin;sudo chmod -R 755 /usr/local/bin/*")
    else:
        print('Package Error')
        sys.exit(1)


def commands():
    if len(sys.argv) < 2:
        print('no argument')
        sys.exit(1)
    action = sys.argv[1]

    if action == 'search':
        package = sys.argv[2]
        read_package_list(package)
    elif action == 'install':
        package = sys.argv[2]
        url = read_package_list(package)
        print(url)
        download_file(url)
        install(package)
    elif action == 'list':
        pack_list = package_list()
        print(f'{pack_list}')


def main():
    system = system_platform()
    commands()
    if system == 'linux':
        # linux_shell()
        pass
    elif system == 'darwin':
        # mac_shell()
        pass


if __name__ == '__main__':
    if os.name == 'posix' and os.getuid() != 0:
        print('ERROR: You must run as root!')
        sys.exit(1)
    main()
