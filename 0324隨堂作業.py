#!/usr/bin/env python
# -*- coding: big5 -*-
f=open("record.txt","r")
count={}
for line in f:
 line=line.replace('\r\n',' ')
 token=line.split(',')
 if count.has_key(token[0]):
  count[token[0]]=count[token[0]]+token[1]
 else:
  count[token[0]]=token[1]
#print token
#print token[0]+' => 'token[1]

for i in count.keys():
 print i+'==>'+count[i]
#print count