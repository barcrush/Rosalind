#!/usr/bin/env python3

"""
###Bioinformatics Armory###
Rosalind: Pairwise Global Alignment
URL: https://rosalind.info/problems/need/

Problem
Given: Two GenBank IDs.
Return: The maximum global alignment score between the DNA strings associated with these IDs.
"""

from Bio import Entrez, SeqIO, pairwise2

## Option 1:
# Read the Genbank IDs
with open("data/rosalind_need.txt", "r") as f:
    genbank_ids = ", ".join(f.readline().strip().split())

# Email setup
Entrez.email = "**@******"

# Retrieve the plain text records in FASTA format from the NCBI database
handle = Entrez.efetch(db="nucleotide", id=[genbank_ids], rettype="fasta")

# Store in record obj
records = list(SeqIO.parse(handle, "fasta"))

#   
print(pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2])

"""
## Option 2:
from Bio import Entrez, SeqIO
import Bio.Emboss.Applications

def main():
    Entrez.email = 'mr.maithania@gmail.com'
    #Entrez.email = input('Please specify an email address for the NCBI database:\n').strip()
    
    # Read in two GenBank IDs.
    with open('data/rosalind_need.txt', 'r') as infile:
        gen_ids = infile.read().strip().split(' ')
    
    # Retrieve the plain text records in FASTA format from the NCBI database
    handle = Entrez.efetch(db='nucleotide', id=gen_ids, rettype='fasta')
    
    # Parse the records into a useable list
    records = list(SeqIO.parse(handle, 'fasta'))
    
    # Output fasta files
    for i, record in enumerate(records):
        out_handle = 'output/temp' + str(i) + '.fasta'
        SeqIO.write(record, out_handle, 'fasta')
        
    # Get needle output
    pair = Bio.Emboss.Applications.NeedleCommandline('output\temp1.fasta')
    print(pair)

if __name__ == '__main__':
    main()
"""