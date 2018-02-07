# -*- coding: utf-8 -*-

'''
3、保留字
什么是保留字？
就是python官方已经保留下来的关键字，不允许开发者使用
就像生活中，如果我们开个银行，是不允许叫中国人民银行的，也不允许叫中国工商银行
这些名字，官方已经使用了。
 在生活中我们使用这些名字会犯法，在程序中我们使用保留字的后果就是语法错误。
 
 那么保留字都有哪些呢？

 ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
 
'''

import keyword
print (keyword.kwlist)