#!/usr/bin/env python
# -*- coding: big5 -*-
def guess_number():
	number=input("Please enter a number:")
	a=1
	b=99
	x=[0,1]
	if number==lucky_number:
		print u"Bingo!!終極密碼是%d" %number
	elif number<lucky_number:
		x[0]=a
		print "%d~%d" %(a,b)
		guess_number()
	else:  
		x[1]=b	
		print "%d~%d" %(a,b)                   
		guess_number()
	
	
	
		
import random
lucky_number=random.randint(1,99)
guess_number()
 