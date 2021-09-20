# PYTHON_ARGCOMPLETE_OK
# PYZSHCOMPLETE_OK
import argparse as _arg
from argparse import RawTextHelpFormatter
import argcomplete as _auto
import pyzshcomplete as _auto_zsh
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

    def linux_shell(self, package, install=False, uninstall=False, update=False, verbose=False):
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

    def mac_shell(self, package, install=False, uninstall=False, update=False, verbose=False):
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
        cmd = f"temp=/tmp;a=`ls $temp | grep '^dpm_{package}'`;tar -xf $temp/$a -C $temp package.json;cat $temp/package.json;rm -rf $temp/package.json"
        output = subprocess.Popen(
            cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = output.stdout.read()
        data_json = json.loads(data.decode("utf-8"))
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
    def install_update(self, package):
        if os.path.isdir(f"/usr/local/DPM/{package}") and os.path.isfile(f"/usr/local/bin/{package}"):
            error = os.system(
                f'sudo rm -rf /usr/local/bin/{package} /usr/local/DPM/{package}')
            if error == 0:
                local = os.system(
                    f"sudo mkdir -p /usr/local/DPM/{package};sudo chown -R $USER /usr/local/DPM/*")
                if local == 0:
                    file = os.system(f"cd /tmp;ls | grep '^dpm_{package}'")
                    if file == 0:
                        download = package_download()
                        info = download.read_package_info(package)
                        os.system(
                            f"temp=/tmp;a=`ls $temp | grep '^dpm_{package}'`;tar -xf $temp/$a -C /usr/local/DPM/{package};sudo chmod -R 555 /usr/local/DPM/*;sudo ln -s /usr/local/DPM/{package}/{info['main_file']} /usr/local/bin/{package};rm $temp/$a")
                    else:
                        print('Package NO Found')
                        sys.exit(1)
            else:
                print('Package Error')
                sys.exit(1)

    def install(self, package):
        download = package_download()
        is_my = download.package_list()
        if package in is_my:
            url = download.read_package_list(package)
            download.download_file(url)
            local = os.system(
                f"sudo mkdir -p /usr/local/DPM/{package};sudo chown -R $USER /usr/local/DPM/*")
            if local == 0:
                file = os.system(f"cd /tmp;ls | grep '^dpm_{package}'")
                if file == 0:
                    info = download.read_package_info(package)
                    os.system(
                        f"temp=/tmp;a=`ls $temp | grep '^dpm_{package}'`;tar -xf $temp/$a -C /usr/local/DPM/{package};sudo chmod -R 555 /usr/local/DPM/*;sudo ln -s /usr/local/DPM/{package}/{info['main_file']} /usr/local/bin/{package};rm $temp/$a")
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
        if package is None:
            os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/derrick921213/Derrick_package_manager-DPM-/main/bin/update.sh?$(date +%s))"')
            print(f"[DPM] self update successfully!!")
        else:
            download = package_download()
            is_my = download.package_list()
            if package in is_my:
                if len(download.installed_package_list()) > 0:
                    if os.path.isdir(f"/usr/local/DPM/{package}"):
                        if os.path.isfile(f"/usr/local/DPM/{package}/package.json"):
                            with open(f"/usr/local/DPM/{package}/package.json", "r") as f:
                                installed_info = json.loads(f.read())
                                download = package_download()
                                download.download_file(
                                    download.read_package_list(package))
                                info = download.read_package_info(package)
                                if info["version"] > installed_info["version"]:
                                    self.install_update(package)
                                else:
                                    print(f"[{package}] no update!!")
                        else:
                            print(f"[{package}] Update Error")
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
    def __init__(self, args, package, verbose=False):
        self.__commands(args, package, verbose)

    def __commands(self, args, package, verbose):
        act = Action()
        _package = " ".join(package)
        if args == "install":
            act.install(_package)
        elif args == "uninstall":
            act.uninstall(_package)
        elif args == "list":
            package_download().installed_package_list()
        elif args == "search":
            if 'list' in package[0] or 'ls' in package[0]:
                download = package_download()
                packages = download.package_list()
                print('---------------')
                for keys in packages.keys():
                    print(keys)
                print("----These package can install from repository----")
            else:
                package_download().read_package_list(_package)
        elif args == "update":
            act.update(_package)


if __name__ == '__main__':
    parser = _arg.ArgumentParser(
        prog="dpm", description="DPM is a package manager", formatter_class=RawTextHelpFormatter, epilog="Further help: \n  https://github.com/derrick921213/Derrick_package_manager-DPM-")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="開啟囉唆模式")
    parser.add_argument("commands",  choices=('search', 'install', 'list',
                        'uninstall', 'update'), help="Choose one command to execute!")
    parser.add_argument("package", nargs='*',
                        help="Wants to use packages or command")
    _auto.autocomplete(parser)
    _auto_zsh.autocomplete(parser)
    args = parser.parse_args()
    if args.verbose:
        main(args.commands, args.package, verbose=True)
    else:
        main(args.commands, args.package)
