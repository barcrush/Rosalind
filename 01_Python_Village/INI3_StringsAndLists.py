#!/usr/bin/env python3

"""
Problem
url: http://rosalind.info/problems/ini3/

Given: A string s of length at most 200 letters and four integers a, b, c and d.
Return: The slice of this string from indices a through b and c through d (with space in between),
inclusively.

"""
with open('data/rosalind_ini3.txt') as input_data:
	s, points = [line.strip() for line in input_data.readlines()]
	a,b,c,d = map(int, points.split())

slices = [s[a:b+1], s[c:d+1]]

print(' '.join(slices))