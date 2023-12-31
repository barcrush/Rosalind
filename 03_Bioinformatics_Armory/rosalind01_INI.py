#!/usr/bin/env python3

"""
###Bioinformatics Armory###
Problem: Introduction to the Bioinformatics Armory
URL: http://rosalind.info/problems/ini/

Given: A DNA string s of length at most 1000 bp.
Return: Four integers (separated by spaces) representing the respective number
of times that the symbols 'A', 'C', 'G', and 'T' occur in s. 
Note: You must provide your answer in the format shown in the sample output below.
"""
from Bio.Seq import Seq


def main():
    # Read the input file
    with open('data/rosalind_ini.txt', 'r') as fh:
        seq = Seq(fh.readline())

    # Count the number of each nucleotide
    counts = map(seq.count, ['A', 'C', 'G', 'T'])

    # print the answer
    print(' '.join(map(str, counts)))


if __name__ == '__main__':
    main()