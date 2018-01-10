#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/1/10 下午11:08
# @Author  : tsgkim
# @Site    : 
# @File    : GuessSize.py.py
# @Software: PyCharm

import random

s = int(random.uniform(1, 10))
print '随机数为：', s
m = int(input('请输入整数：'))
print '输入数为：', m, 'hello world!'

while m != s:
    if m > s:
        print '大了！'
        m = int(input('请输入整数：'))
    if m < s:
        print '小了！'
        m = int(input('请输入整数：'))
    else:
        print '答对了！'