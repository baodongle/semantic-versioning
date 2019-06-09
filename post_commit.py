#!/usr/bin/env python3
from os.path import isfile

from main import Version

try:
    if isfile('VERSION'):
        with open('VERSION', 'r+') as f:
            content = f.read()
            version = Version(content)
            version.patch += 1
            f.seek(0)
            f.truncate()
            f.write(str(version))
    else:
        with open('VERSION', 'w') as f:
            f.write('1.0.1')
except OSError:
    print('Error occurred when access file VERSION')
except TypeError:
    print(f'{content} is not a valid version')
