#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  prime-pal.py
#  
#

import cmath

def main():
	print palindromes(seive(1000))[-1]
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

def palindromes(L):
	return filter(palindrome, L)

def palindrome(n):	
	return  int(n) == int(str(n)[::-1])

if __name__ == '__main__':
	main()

