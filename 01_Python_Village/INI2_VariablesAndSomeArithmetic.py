#!/usr/bin/env python3

"""
Problem
url: http://rosalind.info/problems/ini2/

Given: Two positive integers a and b, each less than 1000.
Return: The integer corresponding to the square of the hypotenuse of the right triangle
whose legs have lengths a and b.
"""
import math

with open("data/rosalind_ini2.txt") as fh:
    a, b = map(int, fh.read().strip().split())

print(int(math.pow(a, 2) + math.pow(b, 2)))
