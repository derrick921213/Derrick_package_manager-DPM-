from platform import platform
from sys import platform as plat


def system_platform():
    if plat == 'win32':
        print('Platform_Error:This application only on Linux or Mac')
    return 'linux' if plat == 'linux' else 'darwin'


def main():
    pass
