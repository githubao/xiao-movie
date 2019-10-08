#!/usr/bin/env python
# encoding: utf-8

"""
@description: 统计个数

@author: baoqiang
@time: 2019/3/17 下午12:57
"""

from collections import defaultdict
import os


def count_sum():
    """
    #########################
    total movies: 174
    #########################
    要看的电影 -> 7
    看过的电影 -> 147
    看过的电视剧 -> 20
    #########################
    看过的电影-动画片 -> 34
    看过的电影-故事片 -> 29
    看过的电影-喜剧片 -> 29
    看过的电影-爱情片 -> 19
    看过的电影-人生片 -> 10
    看过的电影-科幻片 -> 10
    看过的电视剧-武侠剧 -> 9
    看过的电影-动作片 -> 7
    看过的电影-悬疑片 -> 5
    要看的电影-动画片 -> 4
    看过的电影-情色片 -> 4
    看过的电视剧-清宫剧 -> 4
    看过的电视剧-爱情剧 -> 4
    要看的电影-故事片 -> 3
    看过的电视剧-喜剧 -> 2
    看过的电视剧-奇幻剧 -> 1
    #########################
    """

    dic = defaultdict(int)

    title = ''
    subtitle = ''

    with open('README.md', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if line.startswith('## '):
                title = line.strip('## ')
                continue

            if line.startswith('### '):
                subtitle = line.strip('### ')
                continue

            if line.startswith('1. '):
                if not title or not subtitle:
                    print('err line: {}'.format(line))
                    continue

                key = '{}-{}'.format(title, subtitle)

                dic[key] += 1

    count = sum(dic.values())
    print_sep()
    print('total movies: {}'.format(count))
    print_sep()

    # 统计大类
    big_dic = defaultdict(int)
    for k, v in dic.items():
        key = k.split('-')[0]
        big_dic[key] += v

    for k, v in big_dic.items():
        print('{} -> {}'.format(k, v))

    # 每个小的分类按照时间排序
    print_sep()
    sorted_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    for k, v in sorted_dic:
        print('{} -> {}'.format(k, v))

    print_sep()


def find_diff():
    """
    豆瓣看过与readme的不同
    :return:
    """
    home = os.environ['HOME']
    filenanme = '{}/Downloads/movies.txt'.format(home)

    doubans = set()
    reads = set()

    with open(filenanme, 'r', encoding='utf-8') as f:
        name = ''

        for line in f:
            if '/' in line:
                name = line.strip().split('/')[0]
            elif '[' in line:
                name = line.strip().split('[')[0]
            else:
                name = line.strip().split(' ')[0]

            name = name.strip()

            if name and name not in doubans:
                doubans.add(name)
            else:
                print('dup: {}'.format(name))

    with open('README.md', 'r', encoding='utf-8') as f:
        start = False

        for line in f:
            if line.startswith('## '):
                if '看过的电影' in line:
                    start = True
                else:
                    start = False

                continue

            if start:
                if line.startswith('1. '):
                    name = line.strip().strip('1. ')

                    if not name:
                        continue

                    if name not in reads:
                        reads.add(name)
                    else:
                        print('dup2: {}'.format(name))

    print('douban({}), read({})\ndiff1:\n{} \ndiff2:\n{}'.
          format(len(doubans), len(reads), '\n'.join(doubans - reads), '\n'.join(reads - doubans)))


def print_sep():
    print('{}'.format('#' * 25))


if __name__ == '__main__':
    count_sum()
    # find_diff()
