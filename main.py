

from dna_toolkit import *
import random


DNASeq = ''.join([random.choice(nucleotides) for nuc in range(50)])


print('\nSequence: {} \n'.format(validateSeq(DNASeq)))
print('1. Length of Seq: {} \n'.format(len(DNASeq)))
print('2. Count nucleotides: {} \n'.format(countNucFrequency(DNASeq)))
print('3. DNA > mRNA transcription: {} \n'.format(transcription(DNASeq)))

print('4. reverse_complement: {} \n'.format(reverse_complement(DNASeq)))

print('5. GC Content: {}% \n'.format(gc_content(DNASeq)))

print('6. GC Content Subsection: {} \n'.format(gc_content_subsec(DNASeq, k=5)))

print('7. Aminoacids Sequence from DNA: {} \n '.format(translate_seq(DNASeq, 0)))

print('8. Codon Usage: {}'.format(codon_usage(DNASeq, 'L')))

print('9. Reading Frames:')
for frame in gen_reading_frames(DNASeq):
    print(frame)


# print(proteins_from_rf(frame))

print(' \n 10. All protiens for 6 frames: \n ')

for proteins in all_proteins_from_orfs(NM_000207_3, 0, 0, True):
    print(proteins)
