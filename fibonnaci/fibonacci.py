#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fibonacci.py
#  

import sys

def main():
	
	f = open(sys.argv[1])
	
	for line in f:
		n = [int(x) for x in line.split()]
		print fib(n[0])
	
	return 0
		
def fib(n):
	fibnumbers = [0, 1]
	
	for x in range(2,n+1):
		fibnumbers.append(fibnumbers[x-1] + fibnumbers[x-2])
	
	return fibnumbers[-1]

if __name__ == '__main__':
	main()

