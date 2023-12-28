#!/usr/bin/env python3
"""
Working with Files
url: http://rosalind.info/problems/ini5/

Given: A file containing at most 1000 lines.
Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
"""
counter = 0
for line in open('data/rosalind_ini5.txt', "r"):
    if counter % 2 == 1:
        print(line.strip()) #.strip() removes any trailing whitespace/newlines
    counter += 1