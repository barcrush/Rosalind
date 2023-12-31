#!/usr/bin/env python3

""" 
###Bioinformatics Armory###
Rosalind: Complementing a strand of DNA
URL: https://rosalind.info/problems/rvco/

Problem:
Given: A collection of n(n≤10) DNA strings.
Return: The number of given strings that match their reverse complements.
"""
from Bio import SeqIO

with open('data/rosalind_rvco.txt') as fh:
	# Check if the dna sequence matches its complement, add #Trues to get the number
	rev_comp_match = sum([str(dna.seq) == str(dna.reverse_complement().seq) for dna in SeqIO.parse(fh, 'fasta')])
	print(rev_comp_match)