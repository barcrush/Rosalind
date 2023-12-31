#!/usr/bin/env python3

"""
###Bioinformatics Armory###
Rosalind: New Motif Discovery
URL: https://rosalind.info/problems/meme/

The novel-motif finding tool MEME can be found here:
http://meme-suite.org/tools/meme

Given: A set of protein strings in FASTA format that share some motif with minimum length 20.
Return: Regular expression for the best-scoring motif.
"""

meme =""" \
********************************************************************************
MEME - Motif discovery tool
********************************************************************************
MEME version 5.5.5 (Release date: Thu Sep 14 08:48:04 2023 +1000)

For further information on how to interpret these results please access https://meme-suite.org/meme.
To get a copy of the MEME Suite software please access https://meme-suite.org.

********************************************************************************


********************************************************************************
REFERENCE
********************************************************************************
If you use this program in your research, please cite:

Timothy L. Bailey and Charles Elkan,
"Fitting a mixture model by expectation maximization to
discover motifs in biopolymers",
Proceedings of the Second International Conference on Intelligent Systems
for Molecular Biology, pp. 28-36, AAAI Press, Menlo Park, California, 1994.
********************************************************************************
--------------------------------------------------------------------------------
	Motif YQPARIKEFAK MEME-3 regular expression
--------------------------------------------------------------------------------
[YQ][ALQ][PC][AGV]R[IR][KV][ERS]F[AMN][KC]
--------------------------------------------------------------------------------
"""
import re

with open("data/rosalind_meme.txt", "r") as fh:
    for l in fh.readlines():
        meme = l.rstrip()
        print(meme)
        # Find the line containing 'regular expression'
        regex_line_match = re.search(r'>Rosalind_6708', meme)
        print(regex_line_match)
        if regex_line_match:
            # Find the next non-empty line after the line containing 'regular expression'
            next_line_match = re.search(r'[^\s-]+', meme[regex_line_match.end():])
            
            # Print the next non-empty line
            print(next_line_match.group(0).strip() if next_line_match else "Next line not found.")
