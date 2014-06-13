#!/usr/bin/env python
from hashlib import md5
from time import time
from math import floor


KEY_LENGTH = 16
SECRET = ''
PIN = ''


def get_token():
    if len(SECRET) != KEY_LENGTH:
        return False
    m = md5()
    m.update(str(int(floor(time() / 10))) + SECRET + PIN)
    mhex = m.hexdigest()
    return mhex[:6]


def _main():
    token = get_token()
    print(token)


if __name__ == '__main__':
    _main()
