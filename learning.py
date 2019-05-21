#!/usr/bin/env python
# encoding: utf-8

"""
@description: 读取文件

@author: baoqiang
@time: 2019-04-09 23:00
"""

# print "124"

# for abc in [4, 2, 3]:
#     print abc

# for tah in "234":
#     print tah

filename = '/Users/baoqiang/Downloads/1.txt'
filename2 = '/Users/baoqiang/Downloads/2.txt'

f = open(filename, 'r', encoding='utf-8')

# for line in f:
#     print line

lines = f.readlines()
print(lines)

output = set(lines)

print(output)

fw = open(filename2, 'w', encoding='utf-8')

for i in output:
    fw.write(i)

fw.close()

a = 1
