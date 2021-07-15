from sys import platform as plat
from urllib.request import urlopen
import json
import sys
import os


class system_shell:
    def system_platform(self):
        if plat == 'win32':
            print('Platform_Error:This application only on Linux or Mac')
            sys.exit(1)
        return 'linux' if plat == 'linux' else 'darwin'

    def linux_shell(self, package, install=False, uninstall=False, update=False):
        if install is True and uninstall is False and update is False:
            if os.system("which apt >/dev/null") == 0:
                if os.system(f"sudo apt install {package} -y") == 0:
                    print(f'[{package}] Install from apt')
            elif os.system("which dnf >/dev/null") == 0:
                if os.system(f"sudo dnf install {package} -y") == 0:
                    print(f'[{package}] Install from dnf')
            elif os.system("which yum >/dev/null") == 0:
                if os.system(f"sudo yum install {package} -y") == 0:
                    print(f'[{package}] Install from yum')
            else:
                print('Package manager not found')
        elif install is False and uninstall is True and update is False:
            if os.system("which apt >/dev/null") == 0:
                if os.system(f"sudo apt remove {package} -y") == 0:
                    print(f'[{package}] Uninstall from apt')
            elif os.system("which dnf >/dev/null") == 0:
                if os.system(f"sudo dnf install {package} -y") == 0:
                    print(f'[{package}] Uninstall from dnf')
            elif os.system("which yum >/dev/null") == 0:
                if os.system(f"sudo yum remove {package} -y") == 0:
                    print(f'[{package}] Uninstall from yum')
            else:
                print('Package manager not found')
        elif install is False and uninstall is False and update is True:
            if os.system("which apt >/dev/null") == 0:
                if os.system(f"sudo apt update {package} -y") == 0:
                    print(f'[{package}] update from apt')
            elif os.system("which dnf >/dev/null") == 0:
                if os.system(f"sudo dnf update {package} -y") == 0:
                    print(f'[{package}] update from dnf')
            elif os.system("which yum >/dev/null") == 0:
                if os.system(f"sudo yum update {package} -y") == 0:
                    print(f'[{package}] update from yum')
            else:
                print('Package manager not found')
        else:
            print("Application Error")

    def mac_shell(self, package, install=False, uninstall=False, update=False):
        if install is True and uninstall is False and update is False:
            if os.system("which brew >/dev/null") == 0:
                if os.system(f"brew install {package}") == 0:
                    print(f'[{package}] Install from Homebrew')
            else:
                print('Homebrew not found')
        elif install is False and uninstall is True and update is False:
            if os.system(f"brew uninstall {package}") == 0:
                print(f'[{package}] was Removed from Homebrew')
            else:
                print(f"Remove [{package}] Error!!")
        elif install is False and update is False and update is True:
            if os.system(f"brew upgrade {package}") == 0:
                print(f'[{package}] was Upgraded from Homebrew')
            else:
                print(f"Upgrade [{package}] Error!!")
        else:
            print("Application Error")


class package_download:
    def read_package_list(self, package):
        data_json = self.package_list()
        if package in data_json:
            print(f'[{package}] Found!!')
            return data_json[package]["url"]
        else:
            print(f'[{package}] not found!!')

    def read_package_info(self, package):
        import subprocess
        cmd = f"temp=/tmp;a=`ls $temp | grep '^dpm_{package}'`;cat `tar -tf $temp/$a | grep 'package.json'`"
        output = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = output.stdout.read().decode('utf-8')
        data_json = json.loads(data)
        return data_json

    def package_list(self):
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        url = "https://raw.githubusercontent.com/derrick921213/package_manager_server/main/package.json"
        response = urlopen(url)
        data = json.loads(response.read())
        response.close()
        return data

    def installed_package_list(self):
        installed_package = os.listdir('/usr/local/DPM')
        packages = len(installed_package)
        if packages > 0:
            for i in installed_package:
                print(f"{i}")
            return installed_package
        else:
            print("Try install some package")
            sys.exit(1)

    def download_file(self, url):
        import requests as req
        filename = url.split('/')[-1]
        r = req.get(url, stream=True)
        with open("/tmp/"+filename, 'wb') as f:
            f.write(r.content)
        return filename


class Action:
    def install(self, package):
        download = package_download()
        is_my = download.package_list()
        if package in is_my:
            url = download.read_package_list(package)
            print(url)
            download.download_file(url)
            local = os.system(
                f"sudo mkdir -p /usr/local/DPM/{package};sudo chown -R $USER /usr/local/DPM/*")
            if local == 0:
                file = os.system(f"cd /tmp;ls | grep '^dpm_{package}'")
                if file == 0:
                    info = download.read_package_info(package)
                    os.system(
                        f"temp=/tmp;a=`ls $temp | grep '^dpm_{package}'`;tar -xvf $temp/$a -C /usr/local/DPM/{package};sudo chmod -R 555 /usr/local/DPM/*;sudo ln -s /usr/local/DPM/{package}/{info['main_file']} /usr/local/bin;rm $temp/$a")
                else:
                    print('Package NO Found')
                    sys.exit(1)
            else:
                print('Package Error')
                sys.exit(1)
        else:
            shell = system_shell()
            system = shell.system_platform()
            if system == 'linux':
                shell.linux_shell(package, install=True)
            elif system == 'darwin':
                shell.mac_shell(package, install=True)

    def uninstall(self, package):
        download = package_download()
        is_my = download.package_list()
        if package in is_my:
            if len(download.installed_package_list()) > 0:
                if os.path.isdir(f"/usr/local/DPM/{package}"):
                    if os.system(f"sudo rm -rf /usr/local/DPM/{package} /usr/local/bin/{package}") == 0:
                        print(f"[{package}] Removed!!")
                    else:
                        print(f"Remove [{package}] Error!!")
                else:
                    print(f'[{package}] not installed')
        else:
            shell = system_shell()
            system = shell.system_platform()
            if system == 'linux':
                shell.linux_shell(package, uninstall=True)
            elif system == 'darwin':
                shell.mac_shell(package, uninstall=True)

    def update(self, package=None):
        if package == None:
            os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/bin/update.sh?$(date +%s))"')
            print(f"[DPM] self update successfully!!")
        else:
            download = package_download()
            is_my = download.package_list()
            if package in is_my:
                if len(download.installed_package_list()) > 0:
                    if os.path.isdir(f"/usr/local/DPM/{package}"):
                        pass
                    else:
                        print(f"[{package}] not installed")
                else:
                    print(f'[{package}] install first')
            else:
                shell = system_shell()
                system = shell.system_platform()
                if system == 'linux':
                    shell.linux_shell(package, update=True)
                elif system == 'darwin':
                    shell.mac_shell(package, update=True)

    def help(self):
        print('''[DPM] commands
    dpm install   ----Install package
    dpm search    ----Search package
    dpm uninstall ----Uninstall package
    dpm list      ----List installed package
    dpm help      ----This help page
    dpm update    ----Update package
    ''')


class main:
    def __init__(self):
        self.commands()

    def error(self):
        try:
            package = sys.argv[2]
            return package
        except IndexError:
            Action().help()
            sys.exit(1)

    def commands(self):
        if len(sys.argv) < 2:
            Action().help()
        else:
            action = sys.argv[1]
            if action == 'search':
                package = self.error()
                if package == 'list':
                    download = package_download()
                    packages = download.package_list()
                    print('---------------')
                    for keys in packages.keys():
                        print(keys)
                    print("----These package can install from repository----")
                else:
                    download = package_download()
                    download.read_package_list(package)
            elif action == 'install':
                package = self.error()
                Action().install(package)
            elif action == 'list':
                download = package_download()
                download.installed_package_list()
            elif action == 'uninstall':
                package = self.error()
                Action().uninstall(package)
            elif action == 'help':
                Action().help()
            elif action == 'update':
                Action().update()
            else:
                Action().help()


if __name__ == '__main__':
    main()
