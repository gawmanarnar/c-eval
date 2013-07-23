#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  untitled.py
# 



def main():
	print count_combs(21, 0, [], None)
	return 0
	
def count_combs(left, i, comb, add):
    denominations = [8, 7, 6, 3, 2]
    names = {8: "Touchdown /w Two Point Conversion", 7: "Touchdown /w Extra Point", 6 : "Touchdown", 3 : "Field Goal", 2 : "Safety"}
    if add: comb.append(add)
    if left == 0 or (i+1) == len(denominations):
        if (i+1) == len(denominations) and left > 0:
            comb.append( (left, denominations[i]) )
            i += 1
        while i < len(denominations):
            comb.append( (0, denominations[i]) )
            i += 1
        print " ".join("%d %s" % (n,names[c]) for (n,c) in comb)
        return 1
    cur = denominations[i]
    return sum(count_combs(left-x*cur, i+1, comb[:], (x,cur)) for x in range(0, int(left/cur)+1))


if __name__ == '__main__':
	main()

