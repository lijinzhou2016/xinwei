# -*- coding: UTF-8 -*-

import string
a = raw_input("Please input a string: ")
yinwen = 0
kongge = 0
shuzi = 0
qita = 0
for i in a:
    if i.isalpha():
        yinwen = yinwen + 1
    elif i.isdigit():
        shuzi = shuzi + 1
    elif i.isspace():
        kongge = kongge + 1
    else:
        qita = qita + 1

print "%s 有英文字母%s个,空格%s个，数字%s个，其他%s个"%(a,yinwen,kongge,shuzi,qita)