#!/usr/bin/env python
# -*- coding: utf-8 -*-
money=5000
print u"請輸入欲領出的金額:"
a=raw_input('')
num=int(a)
total=(money-num)
if total<0:
	print u"您的存款不足!!" 
	
	f=open("ATM.txt","a")
	f.write('您的存款不足!!\n')
	f.close()
elif total==0:
	print u"您的存款無剩餘存款"
	f=open("ATM.txt","a")
	f.write('您的存款不剩餘存款\n')
	f.close()
else:
	print u"您的存款還剩 %d 元" %total
	f=open("ATM.txt","a")
	f.write('您的存款還剩 %d 元\n' %total)
	f.close()