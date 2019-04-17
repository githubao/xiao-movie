#!/usr/bin/env python
# encoding: utf-8

"""
@description: sep secret

@author: pacman
@time: 2019/4/17 21:31
"""

filename = 'C:\\Users\\xiaobao\\Downloads\\secret.txt'


def process_secret():
    secret = set()

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if ' ' in line:
                attrs = line.split(' ')

                if len(attrs) != 3:
                    print('err format {}\n'.format(line))
                    continue

                name = attrs[0]
            else:
                name = line

            if name in secret:
                print('repeat {}\n'.format(line))

            secret.add(name)

    print('secret count: {}'.format(len(secret)))

    print('\n'.join(secret))


def main():
    process_secret()


if __name__ == '__main__':
    main()
