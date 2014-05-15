#!/usr/bin/python
x = 0;

for z in range(1,10001):
	if((z%2==0) or (z%3==0) or (z%7==0)):
		x+=1

print x