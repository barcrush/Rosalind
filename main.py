import tarfile

file = "test.txt"
with open(file, "r") as fh:
    for idx, line in enumerate(fh):
        lines = line.rstrip("\n")
        if (idx + 1) % 2 == 0:
            line.split()
            # print(line)

test_str = """
When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of 
"""
mystr = "We tried list and we tried dicts also we tried Zen"
word = None
counts = {}
words = test_str.split()
for word in words:
    counts[word] = counts.get(word, 0) + 1

import pprint
pp = pprint.PrettyPrinter()

# query = str(input("sequence= "))
def complement(nuc):
    nucleotides = "ACGT"
    complements = "TGCA"
    i = nucleotides.find(nuc)
    if i >= 0:
        comp = complements[i]
    else:
        comp = nuc
    return comp

def reverse_complement(seq):
    newseq = ""
    for nuc in seq:
        newseq = complement(nuc) + newseq
    return newseq

# print("The desired sequence is", reverse_complement(query))

hamming = "ASAS"
hamming2 = "ASAA"

distance = sum(s1 != s2 for s1, s2 in zip(hamming, hamming2))
print(distance)

count=0
hdist=0
while count < len(hamming):
    if hamming[count] != hamming2[count]:
        hdist += 1
    count += 1

print(hdist)
