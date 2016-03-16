#!/usr/bin/env python
# -*- coding: utf-8 -*-
print u"請輸入一個數字:"
r=raw_input()
num=int(r)

i=1
while i<=num:
  b=0
  j=1
  while j<=num:
    if num%j==0:
	b=b+1
    j=j+1
  if b==2:
	print u'%d 是質數' %num
	break
  else:
	print u'%d 不是質數' %num
	break