from dna_toolkit import *
import random


rndDNASeq = ''.join([random.choice(nucleotides) for nuc in range(20)])


print('Sequence: {}'.format(validateSeq(rndDNASeq)))
print('1. Length of Seq: {} \n'.format(len(rndDNASeq)))
print('2. Count nucleotides: {} \n'.format(countNucFrequency(rndDNASeq)))
print('3. DNA > mRNA transcription: {} \n'.format(transcription(rndDNASeq)))

print('4. reverse_complement: {}'.format(reverse_complement(rndDNASeq)))
