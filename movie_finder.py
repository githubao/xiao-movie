#!/usr/bin/env python
# encoding: utf-8

"""
@description: 随机豆瓣电影日历

@author: baoqiang
@time: 2019/10/12 1:53 下午
"""

import pandas as pd
from IPython.display import display
from tabulate import tabulate
from urllib.parse import quote

pd.set_option('display.width', 500)


def random_movies():
    """
    type: 0-没看过 1-看过 2-不看
    :return:
    """

    df = pd.read_csv('豆瓣电影日历.csv', index_col='id')
    df = df[df['type'] == 0]
    lucky = df.sample(3)

    # display(lucky)
    # print(lucky.to_html())

    # print(tabulate(lucky, headers='keys', tablefmt='psql'))

    for idx, row in lucky.iterrows():
        print('{}\t<{}>{}{}'.format(idx, row.movie, '\t' * 2, build_url(row.movie)))


def build_url(movie):
    movie_fmt = 'https://search.douban.com/movie/subject_search?search_text={}&cat=1002'
    return movie_fmt.format(quote(movie))


if __name__ == '__main__':
    random_movies()
