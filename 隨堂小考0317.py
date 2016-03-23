#!usr/bin/env python
# -*- coding: big5 -*-
def isPrime(A):
	global n
	n = 0
	if A==2:
		n = 1
	else:
		for x in range(2,A):
			if (A%x==0):
				n = 0
				break
			else:
				n = 1
	return n
sum_n = 0
count = 0
for x in range(2,1001):
	if isPrime(x):
		sum_n += x
		count += 1
print "2~1000的質數總合為:%d" %sum_n