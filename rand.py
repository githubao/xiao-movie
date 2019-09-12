#!/usr/bin/env python
# encoding: utf-8

"""
@description: sep secret

@author: pacman
@time: 2019/9/12 21:45
"""

import random
import os

filepath = 'e:/small-movies/torrents/'

def rand():
    lines = os.listdir(filepath)

    print('file count: {}'.format(len(lines)))

    results = random.sample(lines,3)

    print("\n".join(results))
    
if __name__ == "__main__":
    rand()
