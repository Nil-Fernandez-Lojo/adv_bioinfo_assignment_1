from uniprotRetrieve import uniprotRetrieve
from uniprotGroupId import uniprotGroupId
from blast import blast
import pandas as pd

fasta_file = "test_prot.fasta"

#Read sequences in the Fasta file
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


DATABASE="UniRef90"
EVALUE=0.0001
HITS=1000
for prot_number in range(len(sequences)):
    print(prot_number)
    PROTEINLIST = blast(sequences[prot_number],
                            fileName=sequences_name[prot_number]+".list", 
                            database=DATABASE,
                            eValue=EVALUE,
                            hits=HITS,
                            format="list")
    GROUPID=uniprotGroupId(PROTEINLIST,databaseFrom=DATABASE)
    uniprotRetrieve(sequences_name[prot_number]+".fasta", query=GROUPID, format="fasta")
