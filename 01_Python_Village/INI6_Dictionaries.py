#!/usr/bin/env python3

"""
Problem
url: http://rosalind.info/problems/ini6/

Given: A string s of length at most 10000 letters.
Return: The number of occurrences of each word in s, where words are separated by spaces. 
Words are case-sensitive, and the lines in the output can be in any order.
"""
dict = {}

with open('data/rosalind_ini6.txt') as fh:
	words = fh.read().strip().split()
for word in words:
    if word in dict.keys():
        dict[word] += 1
    else:
        dict[word] = 1

for key, value in dict.items():
    print(key, value)