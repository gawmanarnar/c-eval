#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	print points(5)
	return 0
	
def points(n):
	if n < 0:
		return 0
	if n == 0:
		return 1
	
	return points(n-8) + points(n-7) + points(n-6) + points(n-3) + points(n-2)

if __name__ == '__main__':
	main()

