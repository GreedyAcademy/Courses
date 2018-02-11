# -*- coding: utf-8 -*-

'''
python的缩进
python是使用缩进来表示代码块的。 那么什么是缩进呢
就是用空格或者是tab键来表示。
同一代码块的语句，它缩进的空格数必须是相同的。
'''


#下面是一段正确的代码
i = 1
print (i)

if i == 1 :
    print ("right")
else :
    print ("wrong")
    

#如果像下边这样，那就是不对的，代码就会抛出错误    
i = 1
print (i)

if i == 1 :
print ("right")
else :
print ("wrong")