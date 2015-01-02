#!/usr/bin/env python
# -*- coding: cp1251 -*-

#file3= open('./vista_sec.csv','r') #remarked to protect files
#file= open('./vista_sec2.csv','w') #remarked to protect files
messages=file3.readlines()
file3.close()
i=0
k=0
while i<len(messages)-1:
    j=1
    k=0
    while k<len(messages[i]):
	if messages[i][k]=="%":
	    while messages[i][k+1].isdigit():
		messages[i]=messages[i][0:k+1]+messages[i][k+2:]
		print messages[i]
	    messages[i]=messages[i][0:k+1]+str(j)+messages[i][k+1:]
#	    print messages[i]
	    j=j+1
	k=k+1
#    file.write(messages[i]) #remarked to protect files
    i=i+1
	    
    
file.close()