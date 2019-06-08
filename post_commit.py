#!/usr/bin/env python3
from os.path import isfile

try:
    if isfile('VERSION'):
        with open('VERSION', 'r+') as f:
            version = f.read()
            pos = version.rfind('.') + 1
            patch = int(version[pos:]) + 1
            f.seek(pos)
            f.write(str(patch))
    else:
        with open('VERSION', 'w') as f:
            f.write('1.0.1')
except OSError:
    print('Error occurred when access the version file!')
