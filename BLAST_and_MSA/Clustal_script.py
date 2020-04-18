from clustalOmega import clustalOmega

fasta_file = "test_prot.fasta"

f = open(fasta_file, "r")
fl = f.readlines()
f.close()
sequences = []
sequences_name = []
prot_number = 0
for line in fl:
    if line[0] == ">":
        sequences_name.append(line[1:-1])
        if (prot_number!=0): sequences.append(my_seq)
        my_seq = line
        prot_number+=1
    else:
        my_seq+=line
sequences.append(my_seq)

for prot_number in range(len(sequences)):
    print(prot_number,sequences_name[prot_number])
    clustalOmegaFasta,clustalOmegaPim = clustalOmega(sequences_name[prot_number]+".fasta",outputFormat=OUTPUTFORMAT)