file = 'standard.code'
data = {}

with open(file, "r") as fh:
    for line in fh:
        line = line.split()
        headers = line[0]
        sequences = line[2]
        data[headers] = sequences

aa = data['AAs']
b1 = data['Base1']
b2 = data['Base2']
b3 = data['Base3']
metCodon = data['Starts']

codons = {}
initMeth = {}
num = len(b1)   # b2 or b3 any base sequence
for i in range(num):
    codon = (b1[i] + b2[i] + b3[i]).replace("T", "U")
    codons[codon] = aa[i]
    initMeth[codon] = (metCodon == 'M')

aaseq = []
protein = ""
file2 = "test_str"
with open(file2, "r") as fh_in:
    for line in fh_in:
        line = line.rstrip()
        lenseq = len(line)
        for start in range(0, lenseq, 3):
            window = line[start: start + 3].replace("\n", "")
            aa_unit = codons[window]
            aaseq.append(aa_unit)
            protein = "".join(aaseq)

# pp.pprint(codons)
# print(protein)

# Working with reading frames

rf_seq = """
CGAACATAAGCATCATGGGATCGTTACACCAGAAGGTTGAATTGCGCGCGAACTAATGGA
TGGCCGACTTGATAGAGCAGTAATGGTTGCTTTCCGGTCAACAGCCTTTGACTCGGGACT
ATTGATCGGAACTCCATCCAAGCGGCACGCGTAATACAACTAGGTGTCGTTTTAGTGTAG
GCCAACCGCTTCATGTGCAACCAGGACCCATATGAGTCGCAACAGTGATCTCGTTTTGGC
AGTGGCTAACGGCTCCAGCACGTGTCGTATCAGATCGGAGTTTATGCGATCGTTCCGATT
TAAGGGACGACCCCCTACCTCGGTTGAAGGGGGATAATTGCATAGGACGCCGGCTGCCAG
GAATTTTGGGCACTCCCTATGGTTATGCCCTAGAGATTTTATGCTGTGGGTGATAGTCTA
GCTAGACTATCACCCACAGCATAGATGACGTCCTTCCTTCTTTAATAAACTTACGTGAGG
CTTTGTCCAATCTGCGAGGTCCTTCTGAGGAGCCAATCCGGCTCTCAGATCTATTGGAAA
GACCATAGGTCCTGGTGGGGGCGATCACCGCTCCCACAACCCGGCACCCTTAAATTTCGC
AGTTGGAGAGTGATCATAACAATGACGCAGACTTCCGTCAAATGATACACAACAACTGAG
AGAGGTTGTGAGCTCTATATGATACAGTCTGGCAGGTACGATTGGCTCCCGTCTATCAGA
TAGAGTTAGAACAACGTCGAGGGAGCCTCGAAGGTATCAATCCCCCCCTTCGGCGATGCC
GCGCCAGTCCACTAATAGTAGCAAAGATACCAGGGCGATTTGCCGAGGGAACCTTTAACT
CA
"""
rc_seq = """
TGAGTTAAAGGTTCCCTCGGCAAATCGCCCTGGTATCTTTGCTACTATTAGTGGACTGGCGCGGCATCGCCGAAGGGGGGGATTGATACCTTCGAGGCTCCCTCGACGTTGTTCTAACTCTATCTGATAGACGGGAGCCAATCGTACCTGCCAGACTGTATCATATAGAGCTCACAACCTCTCTCAGTTGTTGTGTATCATTTGACGGAAGTCTGCGTCATTGTTATGATCACTCTCCAACTGCGAAATTTAAGGGTGCCGGGTTGTGGGAGCGGTGATCGCCCCCACCAGGACCTATGGTCTTTCCAATAGATCTGAGAGCCGGATTGGCTCCTCAGAAGGACCTCGCAGATTGGACAAAGCCTCACGTAAGTTTATTAAAGAAGGAAGGACGTCATCTATGCTGTGGGTGATAGTCTAGCTAGACTATCACCCACAGCATAAAATCTCTAGGGCATAACCATAGGGAGTGCCCAAAATTCCTGGCAGCCGGCGTCCTATGCAATTATCCCCCTTCAACCGAGGTAGGGGGTCGTCCCTTAAATCGGAACGATCGCATAAACTCCGATCTGATACGACACGTGCTGGAGCCGTTAGCCACTGCCAAAACGAGATCACTGTTGCGACTCATATGGGTCCTGGTTGCACATGAAGCGGTTGGCCTACACTAAAACGACACCTAGTTGTATTACGCGTGCCGCTTGGATGGAGTTCCGATCAATAGTCCCGAGTCAAAGGCTGTTGACCGGAAAGCAACCATTACTGCTCTATCAAGTCGGCCATCCATTAGTTCGCGCGCAATTCAACCTTCTGGTGTAACGATCCCATGATGCTTATGTTCG
"""
# query = input("sequence: ")
# print("Reverse complement", reverse_complement(query))
rf_seq = rf_seq.split()
ex_seq = "".join(rc_seq)
print(len(rc_seq))
first_frame = ex_seq.replace("T", "U")
second_frame = ex_seq[1:-1].replace("T", "U")
third_frame = ex_seq[2:-1].replace("T", "U")

import re
# pattern to find all the reading frames
pattern = re.compile(r'(?=(AUG(?:...)+?(?=UGA|UAA|UAG)))')
result = pattern.findall(first_frame)
# pattern = re.search('AUG([AUGC]{3})+?(UGA|UAA|UAG)', str(first_frame))
# result = pattern.group()

print(result)
print(len(result[0]))

# generating protein sequences of the all reading frames
query = result[0]
ptn_seq = ""
final_seq = []
bcaa = []
seqlen = len(query)
ran = range(0, seqlen, 3)
for x in ran:
    window = query[x: x + 3]
    aminoAcid = codons[window]
    if aminoAcid == '*':
        break
    bcaa.append(aminoAcid)
    ptn_seq = "".join(bcaa)

print(ptn_seq)
print(len(ptn_seq))