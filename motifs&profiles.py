# Finding DNA needles in Genomic Haystacks
""" FINDING MOTIFS IN DNA SEQUENCE """
# Python use 0-based numbering for positions of symbols in strings
import pprint
import re
from typing import List, Any

test_seq = 'GATATATGCATATACTT'
rosalind_seq = """
GTTGCACTATTGCACTACCTAAATCTGCACTATGCACTATTGCACTACTCTGCACTATATTGCACTATGCACTACTGCACTATCCTTGCTGCACTACCCCCTGCTGCACTATCTCTGCACTATGCACTATGCACTATCTCACTGTTGCCCATGGCATGCACTAGTGCACTATGCACTAACACATGCACTAATGCACTATGCACTAATGCACTAGGTGCCTGCACTAGTGCACTAAGACTGCACTAAACATGCACTACCGACGCTCATAGTGCACTACTCGCACCTGCACTATACCTGCACTATGCCATTGCACTATTGCACTATGCACTAATGCACTATTTCTTTCCTGCACTATGCACTAGAGGATCAAAGAGCGATGCACTACTGCACTACCTGCACTATGTGCACTATGCACTACTTGCACTAGGGATCTGCACTAGAACTCAACTTGCACTAGGAAATGCACTATGCACTATGCACTAGTGCACTACAGGGTGTGTGCACTATTGCACTATGCACTAACTCTTGCACTAGAATGTGCACTACTGCACTATGCACTATGCACTAATGCACTATGCACTACGAAGACGATGCACTAATGTGCACTAGTGCACTAGCAAATGCACTATGCACTATTCCTAGTAGTGCACTATGCACTAAATGCACTATTGCACTATGCACTAAGGGTGATGCACTAGACCGTAGTGCACTATAACCCACACTTAGTGCACTAATGCACTATTGCACTAAAGTGCACTAATTGCACTATGCACTATGCACTAGCCCTGCACTATCTGTGCACTATGCACTACATGCACTAGTGCACTAGCCATATGCACTAACTGCACTATGCACTATTGCACTATGCACTAGTGCACTATGCACTAGATGCACTAGTCTTGCACTATGCACTAATTGCACTA
"""


# failed to provide the non-overlapped motifs, but still provide the index for confirmation
result2 = re.finditer("TGCACTATG", string=rosalind_seq, flags=0)

# failed to provide the non-overlapped motifs
rgx = re.findall(r'TGCACTATG', rosalind_seq)

# first approach
for idx in range(len(rosalind_seq)):
    if test_seq[idx:].startswith("TGCACTATG"):
        print(idx + 1)

# second approach
def find_motif(seq_dna, motif):
    return [count.start() for count in re.finditer("(?=" + motif + ")", seq_dna)]


output = find_motif(rosalind_seq, "TGCACTATG")

# ----/----/-----------------
""" Consensus and Profile"""
# Profile matrix is a 4 x n matrix (P), in which P1j represents the no. of times that
# 'A' occurs in jth position of one of the strings, P2j represents 'C', and so on.
# DNA strings, Profile, Consensus
# We need to count the occurrence of each nucleotide at each position, and summarize the
# results in profile matrix.


# using  biopython and numpy
from Bio import SeqIO
sequences = []
handle = open("matrix.fasta", "r")


for record in SeqIO.parse(handle, 'fasta'):
    sequence = []
    for nt in record.seq:
        sequence.extend(nt)
    sequences.append(sequence)
handle.close()

print(len(sequences))
# the below block of code iterates over each nucleotide in each of the sequences and
# counts the number of times they occur at a specific position.
# The results are added continually to the profile matrix

import numpy
profile = numpy.zeros((4, len(sequences[0])), dtype=int)
print(profile)


for i, line in enumerate(sequences):
     for j, nt in enumerate(line):
          if nt == 'A':
               profile[0][j] += 1
          elif nt == 'C':
               profile[1][j] += 1
          elif nt == 'G':
               profile[2][j] += 1
          elif nt == 'T':
               profile[3][j] += 1

# next part conveys that if two nucleotides occur equally many times in a position
# than only the first one in the order given in the program will be added to the consensus
# sequence.

consensus = ''
for A,C,G,T in zip(profile[0],profile[1],profile[2],profile[3]):
     if A >= C and A >= G and A >= T:
          consensus += 'A'
     elif C >= A and C >= G and C >= T:
          consensus += 'C'
     elif G >= A and G >= C and G >= T:
          consensus += 'G'
     elif T >= A and T >= C and T >= G:
          consensus += 'T'

# printing the output
print(consensus)
print('A: ' + ' '.join(str(e) for e in profile[0]))
print('C: ' + ' '.join(str(e) for e in profile[1]))
print('G: ' + ' '.join(str(e) for e in profile[2]))
print('T: ' + ' '.join(str(e) for e in profile[3]))

