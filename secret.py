#!/usr/bin/env python
# encoding: utf-8

"""
@description: sep secret

@author: pacman
@time: 2019/4/17 21:31
"""

from collections import defaultdict

filename = 'C:\\Users\\xiaobao\\Downloads\\secret.txt'


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


def main():
    process_secret()


if __name__ == '__main__':
    main()
