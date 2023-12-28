#!/usr/bin/env python3

"""
Problem: Counting DNA Nucleotides
URL: http://rosalind.info/problems/dna/

Given: A DNA string s of length at most 1000 nt.
Return: Four integers (separated by spaces) counting the respective number of times 
that the symbols 'A', 'C', 'G', and 'T' occur in s
"""

def main():
    # Read the input file.
    with open('data/rosalind_dna.txt', 'r') as infile:
        dna = infile.read()

    # Count the number of each nucleotide
    counts = map(dna.count, ['A', 'C', 'G', 'T'])

    # Print the counts
    print(' '.join(map(str, counts)))


if __name__ == '__main__':
    main()