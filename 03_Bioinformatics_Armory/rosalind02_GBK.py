#!/usr/bin/env python3

"""
###Bioinformatics Armory###
Problem: Genbank Introduction
URL: http://rosalind.info/problems/gbk/

Given: A genus name, followed by two dates in YYYY/M/D format.
Return: The number of Nucleotide GenBank entries for the given genus that
were published between the dates specified.
"""
from Bio import Entrez
from bs4 import BeautifulSoup

#Type 1:
with open("data/rosalind_gbk.txt") as input_data:
	genus, start_date, end_date = [line.strip() for line in input_data.readlines()]

Entrez.email = "barcrush@users.noreply.github.com"
handle = Entrez.esearch(db='nucleotide', term=genus+'[ORGN]', mindate=start_date, maxdate=end_date, datetype='pdat')
record = Entrez.read(handle)

print(record['Count'])

# Type 2:
def get_Nucleotide_GenBank_entries(genus_name, date1, date2):
    Entrez.email = "barcrush@users.noreply.github.com"
    term = '"{}"[Organism] AND ("{}"[Publication Date] : "{}"[Publication Date])'.format(genus_name, date1, date2)
    handle = Entrez.esearch(db="nucleotide", term=term)
    records = handle.read()
    # Use 'lxml' as the parser
    soup = BeautifulSoup(records, 'lxml')
    handle.close()
    return soup.count.text

if __name__ == "__main__":
    with open("data/rosalind_gbk.txt", "r") as f:
        genus_name = f.readline().strip()
        date1 = f.readline().strip()
        date2 = f.readline().strip()
    count = get_Nucleotide_GenBank_entries(genus_name, date1, date2)
    print(count)
