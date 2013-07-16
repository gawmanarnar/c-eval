#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  reverse-words.py
#

import sys
import re

def main():
	
	f = open(sys.argv[1])
	
	for line in f:
		if not line.strip():
			continue
		else:
			r = line.split()
			r.reverse()
			print ' '.join(r)

if __name__ == '__main__':
	main()

