#!/usr/bin/env python3

"""
###Bioinformatics Armory###
Rosalind: Data Formats
URL: http://rosalind.info/problems/frmt/

Given: A collection of n(n≤10) GenBank entry IDs.
Return: The shortest of the strings associated with the IDs in FASTA format.
"""
from Bio import Entrez, SeqIO

with open("data/rosalind_frmt.txt") as input_data:
	IDs = input_data.read().strip().split()

Entrez.email = "jschendel@users.noreply.github.com"
handle = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))

[min_index] = [i for i in range(len(records)) if len(records[i]) == min([len(record.seq) for record in records])]

handle2 = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
minFASTA = handle2.read().strip().split('\n\n')[min_index]

print(minFASTA)