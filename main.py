from dna_toolkit import validateSeq, nucleotides, countNucFrequency
import random


rndDNASeq = ''.join([random.choice(nucleotides) for nuc in range(20)])


print(validateSeq(rndDNASeq))
print(countNucFrequency(rndDNASeq))
