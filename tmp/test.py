'''
        def error(self):
        try:
            package = sys.argv[2]
            return package
        except IndexError:
            Action().help()
            sys.exit(1)
            
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
                package = self.error()
                Action().update(package)
            else:
                Action().help()
        '''
#from function import file_sum_sha256

import os
import sys

sys.path.append(os.getcwd())
import function

print(os.getcwd())
print(function.file_sum_sha256.__name__)
print(function.file_sum_sha256.__package__)
