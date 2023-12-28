#!/usr/bin/env python3

"""
Problem
url: http://rosalind.info/problems/ini4/

Given: Two positive integers a and b (a<b<10000).
Return: The sum of all odd integers from a through b, inclusively.
"""
with open('data/rosalind_ini4.txt') as fh:
	a,b = map(int, fh.read().strip().split())

c = 0
for i in range(a, b+1, 2):
	c += i

print(c)