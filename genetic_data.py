""" computing GC content multiple sequences and finding the sequence
 with the highest content """
# Affect genome functioning and species ecology
# Facilitating more complex gene regulation
# In PCR, GC content allows to predict their annealing temperature to the template DNA
# and indicating relative melting temperatures
# Evidence that mutation is universally biased towards AT in Bacteria (Lynch, Bentley, Parkhil, Sueoka)

fastFile = "test.fasta"
with open(fastFile, "r") as fh_in:
    fh_in = fh_in.readlines()
    header = []
    sequences = []
    current_seq = ""
    for line in fh_in:
        if line[0] == '>':
            header.append(line[1:].rstrip("\n"))
            if current_seq != "":
                # add on the data if there is any
                sequences.append(current_seq)
            current_seq = ""    # reset the variable
        else:
            current_seq += line.rstrip("\n")

    if current_seq:
        sequences.append(current_seq)

bigcount = 0
for key, val in zip(header, sequences):
    count = (val.count("G") + val.count("C")) / len(val) * 100
    print(key, count)
    if count > bigcount:
        bigcount = count

print(bigcount)

