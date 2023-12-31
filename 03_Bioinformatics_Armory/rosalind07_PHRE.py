#!/usr/bin/env python3

"""
###Bioinformatics Armory###
Rosalind: Quality Prevails
URL: https://rosalind.info/problems/phre/

Problem
Given: A quality threshold, along with FASTQ entries for multiple reads.
Return: The number of reads whose average quality is below the threshold.
"""

from Bio import SeqIO

def phre(data):
    count = 0
    with open(data, "r") as f:
        threshold = int(f.readline())
        for record in SeqIO.parse(f, "fastq"):
            quality = record.letter_annotations["phred_quality"]
            average_quality = sum(quality)/len(quality)
            if average_quality < threshold:
                count += 1
    print(count)
    return count

if __name__ == "__main__":
    data = "data/rosalind_phre.txt"
    phre(data)