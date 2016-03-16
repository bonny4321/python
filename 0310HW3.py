#!/usr/bin/env python
# -*- coding: utf-8 -*-
f=open("input.txt")
a=f.readline()
b=len(a)
w=a.count(' ')
print u'總字數%d' %b
print u'空白鍵出現%d次' %w
p=float(w)/b
print u'空白鍵 出現在文字檔的比例=',round(p,7)
c=a.count('e')
print u'e 出現%d 次' %c
r=float(c)/b
print u'e 出現在文字檔的比例=',round(r,7)
	
f.close()