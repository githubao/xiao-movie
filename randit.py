#!/usr/bin/env python
# encoding: utf-8

"""
@description: sep secret

@author: pacman
@time: 2019/9/12 21:45
"""

import random
import os

random_size = 5

def rand_all():
    all_path = 'e:/small-movies/torrents/'
    rand(all_path)

def rand_one():
    ok_path = 'e:/small-movies/00/'
    rand(ok_path)

def rand_two():
    root_path = 'e:/small-movies/'
    
    results = []
    for subpath in ['01','02','03','04']:
        fullpath = os.path.join(root_path,subpath)

        for name in os.listdir(fullpath):
            fullname = os.path.join(fullpath,name)
            results.append(fullname)

    print('file count: {}'.format(len(results)))

    results = random.sample(results,random_size)

    print_sep()
    print("\n".join(results))
    print_sep()


def rand(filepath):
    lines = os.listdir(filepath)

    print('file count: {}'.format(len(lines)))

    results = random.sample(lines,random_size)

    print_sep()
    print("\n".join(results))
    print_sep()

def print_sep():
    print('#'*35)
    
if __name__ == "__main__":
    # rand_all()
    # rand_one()
    rand_two()
