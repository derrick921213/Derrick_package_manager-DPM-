import hashlib


def sha256(path, name):
    f = open(path, 'rb')
    sh = hashlib.sha256()
    sh.update(f.read())
    print(sh.hexdigest(), " ====> ", name)
    f.close()
    return
