#!/usr/bin/env python
# encoding: utf-8

"""
@description: 统计个数

@author: baoqiang
@time: 2019/3/17 下午12:57
"""

from collections import defaultdict


def count_sum():
    """
    #########################
    total movies: 174
    #########################
    要看的电影 -> 26
    看过的电影 -> 129
    看过的电视剧 -> 19
    #########################
    看过的电影-动画片 -> 28
    看过的电影-喜剧片 -> 26
    看过的电影-故事片 -> 25
    看过的电影-爱情片 -> 17
    看过的电影-人生片 -> 10
    看过的电影-科幻片 -> 10
    看过的电视剧-武侠剧 -> 9
    要看的电影-动画片 -> 7
    看过的电影-动作片 -> 7
    要看的电影-故事片 -> 6
    要看的电影-情色片 -> 4
    看过的电影-情色片 -> 4
    看过的电视剧-清宫剧 -> 4
    看过的电视剧-爱情剧 -> 4
    要看的电影-悬疑片 -> 3
    要看的电影-爱情片 -> 2
    要看的电影-科幻片 -> 2
    要看的电影-电视剧 -> 2
    看过的电影-悬疑片 -> 2
    看过的电视剧-喜剧 -> 2
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


def print_sep():
    print('#' * 25)


if __name__ == '__main__':
    count_sum()
