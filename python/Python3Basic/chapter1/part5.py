# -*- coding: utf-8 -*-

'''
数据类型
python中数有四种类型：整数、长整数、浮点数和复数。
int (整数), 如 1
long (长整数) , 比较大的整数
float (浮点数), 如 1.23、3E-2
complex (复数), 如 1 + 2j、 1.1 + 2.2j
'''

#什么是int
'''
整数在python语言中，类型为int型
'''
import sys
print (type(sys.maxsize))
print (type(sys.maxsize+9999999999999999999999999999999999999999999999999))

print (9999999**999999)
print (type(1))
print (type(-1))

print (type(31 ** 310000))




#什么是long

'''
python3 中已经将整数全部统一称为int类型，已经没有long了
long代表的就是长整形，意思就是说非常大的int的类型。
'''

#什么是float
i = 11.1
print (type(i))

#什么是复数
'''
复数的基本形式是a+bi,其中a,b是实数,a称为实部,bi称为虚部,i是虚数单位
a+bi中：a=0为纯虚数,b=0为实数,b不等于0为虚数.
复数集包含了实数集，因而是实数集的扩张。
'''

i = 1 + 2j
print (type(i))
print (i.real)
