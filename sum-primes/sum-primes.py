#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sum-primes.py
#   

import cmath

def main():
	print sum(seive(10000)[:1000])
	return 0
	
def seive(n):
	if n < 2:
		return []
	elif n == 2:
		return [2]
		
	primelist = []
	booleanlist = []
	
	for x in range(n-2):
		booleanlist.append(True)
	
	checks = int(abs(cmath.sqrt(n)))
	
	current = 2
	
	for i in range(checks-1):
		if booleanlist[i]:
			for j in range(i+current, len(booleanlist)-1,current):
				booleanlist[j] = False
		current += 1
	
	for i in range(len(booleanlist)-1):
		if booleanlist[i]:
			primelist.append(i+2)
	
	return primelist

if __name__ == '__main__':
	main()

