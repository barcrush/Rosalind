#!/usr/bin/env python3

"""
###Bioinformatics Armory###
Rosalind: Protein Translation
URL: https://rosalind.info/problems/ptra/

Problem
A detailed list of genetic code variants (codon tables) along with 
indexes representing these codes (1 = standard genetic code, etc.) can be obtained here:
https://www.bioinformatics.org/JaMBW/2/3/TranslationTables.html

Given: A DNA string s of length at most 10 kbp, and a protein string translated by s
Return: The index of the genetic code variant that was used for translation. 
(If multiple solutions exist, you may return any one.)
"""

from Bio.Seq import translate

def genetic_code(dna, protein):
    res = []
    table_ids = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]
    for t in table_ids:
        translation = translate(dna, table=t, to_stop=True)
        print(f"Table {t}: {translation}")
        if translation == protein:
            res.append(t)
    return res

if __name__ == "__main__":
    # string = """
    # ATGGCCATGGCGCCCAGAACTGAGATCAATAGTACCCGTATTAACGGGTGA
    # MAMAPRTEINSTRING
    # """
    # lines = [line for line in string.strip().split('\n')]
    # dna = lines[0]
    # protein = lines[1]  
    # print(dna, protein)
    
    with open("data/rosalind_ptra.txt", "r") as fh:
        lines = [line.strip() for line in fh.readlines()]
        dna = lines[0]
        protein = lines[1] 
    res = genetic_code(dna, protein)
    print("Matching tables:", res)

