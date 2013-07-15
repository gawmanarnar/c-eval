#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fizzbuzz.py
#  
import sys

def main():
	f = open(sys.argv[1])
	
	for line in f:
		a, b, n = [int(x) for x in line.split()]
		for x in range(1,n+1):
			if x % a == 0 and x % b == 0:
				sys.stdout.write("FB ")
			elif x % a == 0:
				sys.stdout.write("F ")
			elif x % b == 0:
				sys.stdout.write("B ")
			else:
				sys.stdout.write(str(x) + " ")
		sys.stdout.write('\n')
		
	f.close()
	
	return 0

if __name__ == '__main__':
	main()

