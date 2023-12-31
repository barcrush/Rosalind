#!/usr/bin/env python3

"""
###Bioinformatics Armory###
Rosalind: Suboptimal local alignment
URL: https://rosalind.info/problems/subo/

The Lalign program for finding multiple alternative matches via suboptimal alignment is available here:
https://www.ebi.ac.uk/Tools/psa/lalign/

Problem
Given: Two DNA strings s and t in FASTA format that share some short inexact repeat r
of 32-40 bp. By "inexact" we mean that r may appear with slight modifications 
(each repeat differ by ≤ 3 changes/indels).
Return: The total number of occurrences of r as a substring of s, followed by the total 
number of occurrences of r as a substring of t.
"""
import re
from Bio import pairwise2
from Bio.pairwise2 import format_alignment

# Read sequences from file
with open("data/rosalind_subo.txt", "r") as file:
    lines = file.readlines()

# Extract sequences from FASTA format
seq1 = "GACTCCTTTGTTTGCCTTAAATAGATACATATTTACTCTTGACTCTTTTGTTGGCCTTAAATAGATACATATTTGTGCGACTCCACGAGTGATTCGTA"
seq2 = "ATGGACTCCTTTGTTTGCCTTAAATAGATACATATTCAACAAGTGTGCACTTAGCCTTGCCGACTCCTTTGTTTGCCTTAAATAGATACATATTTG"
# seq1 = """

# """
# seq2 = """

# """


from Bio import pairwise2

# Read sequences from file
with open("data/sequences.fasta", "r") as file:
    lines = file.readlines()


# Perform local alignment
alignments = pairwise2.align.localxx(seq1, seq2, one_alignment_only=True)

# Extract best alignment
best_alignment = alignments[0]

# Extract aligned sequences
aligned_seq1 = best_alignment.seqA
aligned_seq2 = best_alignment.seqB

# Function to find large sequence repeats (present twice or more)
def find_large_repeats(sequence):
    repeats = []
    min_repeat_length = 32  # Set the minimum repeat length

    i = 0
    while i < len(sequence):
        j = i + 1
        while j < len(sequence) and sequence[j] == sequence[i]:
            j += 1

        repeat_length = j - i
        if repeat_length >= min_repeat_length:
            repeats.append(sequence[i:j])

        i = j

    return repeats

# Find large repeats in aligned sequences
large_repeats_seq1 = find_large_repeats(aligned_seq1)
large_repeats_seq2 = find_large_repeats(aligned_seq2)

# Print aligned sequences
print("Aligned Sequence 1:", aligned_seq1)
print("Aligned Sequence 2:", aligned_seq2)

# Print large repeats
print("Large repeats in aligned seq1:", large_repeats_seq1)
print("Large repeats in aligned seq2:", large_repeats_seq2)
