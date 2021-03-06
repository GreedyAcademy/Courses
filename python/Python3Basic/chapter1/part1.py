#Python的基础语法

#1、字符编码
# -*- coding: utf-8 -*-
'''
那么什么是字符编码呢？ 可以理解成为一个字由不同的语言表示。
就像你好，中文是你好，而英文叫hello，泰国就叫刷我滴卡，日本 空你其瓦等等
而字符编码就是计算机来展现不同文字的语言。我们暂且可以认为utf-8 就是中文的意思

在中国，我们写代码的时候绝大部分都指定字符编码为utf-8
这是一种包含中文的字符编码
其他字符编码包含
 GB2312
 GBK
 Big5
 Unicode
 Base64
等等


'''

#2、注释
'''
什么是注释：不需要计算机理解的语言，但人必须能理解，也就是说给人看的语言。
因为在开发大型项目时，程序的研发必然是由多人配合完成的，人员之间要相互理解对方程序表达了什么意思，人与人之间该怎么配合。
即便某些程序是自己一个人完成的，如果没有注释，那么过了一段时间后，自己也不太理解当时为什么会这样写。 因为一段代码的开发，其实代表了一个人当时的思考模式，很有可能过一段时间自己也不太理解当时为什么这样想的。读一段代码，相当于去理解开发者当时的一段思想。

那么python的注释有三种 
主要分为单行注释和多行注释
单行#
多行“”“ 和‘’‘

'''
#这是注释1
'''
这是注释2
'''

"""
这是注释3
"""