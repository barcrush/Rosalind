#!/usr/bin/env python3

"""
Problem: Counting DNA Nucleotides
URL: http://rosalind.info/problems/rna/

Given: A DNA string t having length at most 1000 nt.
Return: The transcribed RNA string of t
"""
def dna2rna(string):
    return string.replace('T','U')


if __name__ == "__main__":
    with open("../data/rosalind_rna.txt", 'r') as f:
        string = f.readline().strip()
        rst = dna2rna(string)
        print(rst)
