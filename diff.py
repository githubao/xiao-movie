#!/usr/bin/env python
# encoding: utf-8

"""
@description: 找不同

@author: baoqiang
@time: 2019-09-12 21:48
"""

import os
import string
import re
import io
import sys
from collections import defaultdict

sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

letters = string.ascii_lowercase

path = 'e:/small-movies/torrents/'
pat = re.compile('^[A-Z\-_0-9]+$')

def diff():
    files = os.listdir(path)

    codes = set()
    nameCount = defaultdict(int)

    for f in files:
        f = f.split('.')[0]

        attrs = f.split(" ")
        if len(attrs) != 3:
            print('err: {}'.format(f))
            continue

        name = attrs[0]
        code = attrs[1]
        desc = attrs[2]

        nameCount[name] += 1

        if code not in codes:
            codes.add(code)
        else:
            print('dup: {}'.format(code))

        m = pat.match(code)
        if not m:
            # print('fmt: {}'.format(code))
            pass

        desc = desc.split('(')[0]
        if len(desc) != 4:
            # print('desc: {}'.format(f))
            pass

    print('file len: {}'.format(len(codes)))

    sorted_dict = sorted(nameCount.items(),key=lambda x
    : x[1],reverse=True)

    for k,v in sorted_dict:
        if v <= 2:
            break
        print('{} -> {}'.format(k,v))

if __name__ == "__main__":
    diff()
