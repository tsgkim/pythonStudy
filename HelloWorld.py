#!/usr/bin/env python
# -*- coding: utf-8 -*-

print "你好，世界"

# raw_input("按下 enter 键退出，其他任意键显示...\n")

x = "a"
y = "b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串

print counter
print miles
print name

a = b = c = 1
print a,
print b,
print c
a, b, c = 1, 2, "john"
print a,
print b,
print c

strs = 'Hello World!'

print strs  # 输出完整字符串
print strs[0]  # 输出字符串中的第一个字符
print strs[2:5]  # 输出字符串中第三个至第五个之间的字符串
print strs[2:]  # 输出从第三个字符开始的字符串
print strs * 2  # 输出字符串两次
print strs + "TEST"  # 输出连接的字符串

elists = ['runoob', 786, 2.23, 'john', 70.2]
tinyelists = [123, 'john']

print elists  # 输出完整列表
print elists[0]  # 输出列表的第一个元素
print elists[1:3]  # 输出第二个至第三个元素
print elists[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinyelists * 2  # 输出列表两次
print elists + tinyelists  # 打印组合的列表

tuples = ('runoob', 786, 2.23, 'john', 70.2)
tinytuples = (123, 'john')

print tuples  # 输出完整元组
print tuples[0]  # 输出元组的第一个元素
print tuples[1:3]  # 输出第二个至第三个的元素
print tuples[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinytuples * 2  # 输出元组两次
print tuples + tinytuples  # 打印组合的元组

tuples = ('runoob', 786, 2.23, 'john', 70.2)
listss = ['runoob', 786, 2.23, 'john', 70.2]
# tuple[2] = 1000  # 元组中是非法应用
listss[2] = 1000  # 列表中是合法应用
print listss

dicts = {}
dicts['one'] = "This is one"
dicts[2] = "This is two"

tinydicts = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dicts['one']  # 输出键为'one' 的值
print dicts[2]  # 输出键为 2 的值
print tinydicts  # 输出完整的字典
print tinydicts.keys()  # 输出所有键
print tinydicts.values()  # 输出所有值

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c

c = a * b
print "3 - c 的值为：", c

c = a / b
print "4 - c 的值为：", c

c = a % b
print "5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print "6 - c 的值为：", c

a = 10
b = 5
c = a // b
print "7 - c 的值为：", c

a = 21
b = 10
c = 0

if a == b:
    print "1 - a 等于 b"
else:
    print "1 - a 不等于 b"

if a != b:
    print "2 - a 不等于 b"
else:
    print "2 - a 等于 b"

if b != a:
    print "3 - a 不等于 b"
else:
    print "3 - a 等于 b"

if a < b:
    print "4 - a 小于 b"
else:
    print "4 - a 大于等于 b"

if a > b:
    print "5 - a 大于 b"
else:
    print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print "6 - a 小于等于 b"
else:
    print "6 - a 大于  b"

if b >= a:
    print "7 - b 大于等于 a"
else:
    print "7 - b 小于 a"

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c

a = 10
b = 20

if a and b:
    print "1 - 变量 a 和 b 都为 true"
else:
    print "1 - 变量 a 和 b 有一个不为 true"

if a or b:
    print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if a and b:
    print "3 - 变量 a 和 b 都为 true"
else:
    print "3 - 变量 a 和 b 有一个不为 true"

if a or b:
    print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "4 - 变量 a 和 b 都不为 true"

if not (a and b):
    print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
    print "5 - 变量 a 和 b 都为 true"

a = 10
b = 20
lists = [1, 2, 3, 4, 5];

if a in lists:
    print "1 - 变量 a 在给定的列表中 lists 中"
else:
    print "1 - 变量 a 不在给定的列表中 lists 中"

if b not in lists:
    print "2 - 变量 b 不在给定的列表中 lists 中"
else:
    print "2 - 变量 b 在给定的列表中 lists 中"

# 修改变量 a 的值
a = 2
if a in lists:
    print "3 - 变量 a 在给定的列表中 lists 中"
else:
    print "3 - 变量 a 不在给定的列表中 lists 中"

a = 20
b = 20
if a is b:
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if a is not b:
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"

# 修改变量 b 的值
b = 30
if a is b:
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"

if a is not b:
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"

# 例1：if 基本用法
flag = False
name = 'hello'
if name == 'python':  # 判断变量否为'python'
    flag = True  # 条件成立时设置标志为真
    print 'welcome boss'  # 并输出欢迎信息
else:
    print name  # 条件不成立时输出变量名称

# 例2：elif用法
num = 5
if num == 3:  # 判断num的值
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:  # 值小于零时输出
    print 'error'
else:
    print 'hello'  # 条件均不成立时输出

# 例3：if语句多个条件

num = 9
if 0 <= num <= 10:  # 判断值是否在0~10之间
    print 'hello'
# 输出结果: hello

num = 10
if num < 0 or num > 10:  # 判断值是否在小于0或大于10
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

num = 8
# 判断值是否在0~5或者10~15之间
if (0 <= num <= 5) or (10 <= num <= 15):
    print 'hello'
else:
    print 'undefine'
# 输出结果: undefine

var = 100
if var == 100:
    print "变量 var 的值为100"
print "Good bye!"

count = 0
while count < 9:
    print 'The count is:', count
    count = count + 1

print "Good bye!"

i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break

count = 0
while count < 5:
    print count, " is  less than 5"
    count = count + 1
else:
    print count, " is not less than 5"
