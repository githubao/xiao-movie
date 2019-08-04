#!/usr/bin/env python
# encoding: utf-8

"""
@description: sep secret

@author: pacman
@time: 2019/4/17 21:31
"""

from collections import defaultdict
import random
from datetime import datetime
import os
import math

filename = 'C:\\Users\\xiaobao\\Downloads\\secret.txt'
torrent_path = 'C:\\Users\\xiaobao\\Downloads\\torrent'


def compare():
    with open(filename, 'r', encoding='utf-8') as f:
        aset = set(line.strip() for line in f)

    bset = set(s.replace(".torrent", "") for s in os.listdir(torrent_path))

    print(len(aset))
    print(len(bset))

    print('\n'.join(bset - aset))
    print('\n')
    print('\n'.join(aset - bset))


def process_secret():
    secret = set()
    company_dic = defaultdict(int)

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            attrs = line.split(' ')

            if len(attrs) != 3:
                print('err format {}\n'.format(line))
                continue

            name = attrs[0]
            signature = attrs[1]
            company, num = signature.split('-')

            company_dic[company] += 1

            if name in secret:
                print('repeat {}\n'.format(line))

            secret.add(name)

    # 去重之后的个数
    print('secret count: {}'.format(len(secret)))

    # 按公司排序
    sorted_list = sorted(company_dic.items(), key=lambda x: x[1], reverse=True)

    for company, count in sorted_list:
        print('{} -> {}'.format(company, count))

    # print('\n'.join(secret))


def shuf():
    with open(filename, 'r', encoding='utf-8') as f:
        datas = [line.strip() for line in f]

        random.seed(datetime.now())
        luckies = random.sample(datas, 3)

        print('\n'.join(luckies))


def calc():
    # a = 59 * 5 + 1250
    a = 59 * 5 + 1000
    b = 1000
    r = math.pow(a / b, 1 / 5) - 1
    print('{:.12f}%'.format(r * 100))


def main():
    # process_secret()
    # shuf()
    # compare()
    calc()


if __name__ == '__main__':
    main()
