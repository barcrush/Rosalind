#!/usr/bin/env python3

"""
###Bioinformatics Armory###
Rosalind: How to handle Quality
URL: https://rosalind.info/problems/tfsq/

Problem
Given: FASTQ file
Return: Corresponding FASTA records
"""
## Option 1:
from Bio import SeqIO

with open('data/rosalind_tfsq.txt') as input_data, open('output/tfsq_out.txt', 'w') as output_data:
	SeqIO.convert(input_data, 'fastq', output_data, 'fasta' )
	
## Option 2:
import os
os.system("seqtk seq -A data/rosalind_tfsq.txt > output/tfsq_out.fasta")
