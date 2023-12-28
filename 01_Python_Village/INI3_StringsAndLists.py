#!/usr/bin/env python3
"""
Problem
Variables and Some Arithmetic
url: http://rosalind.info/problems/ini2/

Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.
"""
with open('data/rosalind_ini3.txt') as input_data:
	s, points = [line.strip() for line in input_data.readlines()]
	a,b,c,d = map(int, points.split())

slices = [s[a:b+1], s[c:d+1]]

print(' '.join(slices))