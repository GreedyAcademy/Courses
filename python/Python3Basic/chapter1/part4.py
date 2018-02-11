# -*- coding: utf-8 -*-

#多行语句
'''
python的多行语句，指的其实就是一句完整的代码
但是，这行代码太长了，显得不美观
所以要使用多行来表达。 
在企业中，也有一些关于多行语句方面的规范
比如：代码每行的字符数不能超过200
原因是代码太长了，不便于去读代码，不方便也不美观
'''

#下边演示一下如果书写多行语句

#声明一个变量s
s = "s1s2s3s4s5"

s1 = "s1" + \
     "s2" + \
     "s3" + \
     "s4" + \
     "s5"

print (s)
print (s1)
#判断一下s和s1是否相等，如果相等，那么打印Ture
if s == s1:
    print (True)