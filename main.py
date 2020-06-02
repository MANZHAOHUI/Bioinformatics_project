

from dna_toolkit import *
import random


rndDNASeq = ''.join([random.choice(nucleotides) for nuc in range(50)])


print('Sequence: {} \n'.format(validateSeq(rndDNASeq)))
print('1. Length of Seq: {} \n'.format(len(rndDNASeq)))
print('2. Count nucleotides: {} \n'.format(countNucFrequency(rndDNASeq)))
print('3. DNA > mRNA transcription: {} \n'.format(transcription(rndDNASeq)))

print('4. reverse_complement: {} \n'.format(reverse_complement(rndDNASeq)))

print('5. GC Content: {}% \n'.format(gc_content(rndDNASeq)))

print('6. GC Content Subsection: {} \n'.format(gc_content_subsec(rndDNASeq, k=5)))

print('7. Aminoacids Sequence from DNA: {} \n '.format(translate_seq(rndDNASeq, 0)))

print('8. Codon Usage: {}'.format(codon_usage(rndDNASeq, 'L')))
