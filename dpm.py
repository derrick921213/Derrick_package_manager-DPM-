#!/bin/bash

from sys import platform as plat
from urllib.request import urlopen
import json
import sys
import os


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


def installed_package_list():
    installed_package = os.listdir('/usr/local/DPM')
    packages = len(installed_package)
    if packages > 0:
        for i in installed_package:
            print(f"{i}")
    else:
        print("Try install some package")


def download_file(url):
    import requests as req
    from tqdm import tqdm
    filename = url.split('/')[-1]
    r = req.get(url, stream=True)
    with open("/tmp/"+filename, 'wb') as f:
        for data in tqdm(r.iter_content(1024)):
            f.write(data)
    return filename


def install(package):
    local = os.system(
        f"sudo mkdir -p /usr/local/DPM/{package};sudo chown -R $USER /usr/local/DPM/*")
    if local == 0:
        file = os.system(f"cd /tmp;ls | grep '^dpm_{package}'")
        if file == 0:
            success = os.system(
                f"temp=/tmp;a=`ls $temp | grep '^dpm_{package}'`;tar -xzvf $temp/$a -C /usr/local/DPM/{package};chmod -R 555 /usr/local/DPM/*;ln -s /usr/local/DPM/{package}/{package} /usr/local/bin;rm $temp/$a")
        else:
            print('Package NO Found')
            sys.exit(1)
    else:
        print('Package Error')
        sys.exit(1)


def uninstall(package):
    if os.system(f"sudo rm -rf /usr/local/DPM/{package} /usr/local/bin/{package}") == 0:
        print(f"[{package}] Removed!!")
    else:
        print(f"Remove [{package}] Error!!")


def help():
    print('''[DPM] commands
dpm install   ----Install package
dpm search    ----Search package
dpm uninstall ----Uninstall package
dpm list      ----List installed package
dpm help      ----This help page
''')


def commands():
    if len(sys.argv) < 2:
        print('''[DPM] commands
dpm install
dpm search
dpm uninstall
dpm list
dpm help
''')
    else:
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
            installed_package_list()
        elif action == 'uninstall':
            package = sys.argv[2]
            uninstall(package)
        elif action == 'help':
            help()


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
    main()
