from structures import nucleotides, DNA_reverse_complement, DNA_Codons


class bio_seq:
    """docstring for bio_seq."""

    def __init__(self, seq):
        self.seq = seq.upper()

    def validateSeq(self):
        '''Checks if DNA Sequence has the correct letters '''

        for nuc in self.seq:
            if nuc not in nucleotides:
                return False
        return self.seq

    def show_seq_info(self):
        return '\n 1. [Sequence]: {} \n 2. [Length]: {} \n 3. [Biotype]: {}'.format(self.seq, len(self.seq), None)

    def countNucFrequency(self):
        temFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for nuc in self.seq:
            temFreqDict[nuc] += 1
        return temFreqDict

    def transcription(self):
        return self.seq.replace('T', 'U')

    def reverse_complement(self):
        return ''.join([DNA_reverse_complement[nuc] for nuc in self.seq])[::-1]

    def gc_content(self):
        return round((self.seq.count('C') + self.seq.count('G')) / len(self.seq) * 100)

    def gc_content_subsec(self, k=20):
        res = []
        for i in range(0, len(self.seq) - k + 1, k):
            subseq = self.seq[i:i + k]
            res.append(gc_content(subseq))
        return res


# test = bio_seq('XXXXXXXX')
test2 = bio_seq('ACGGGATTTGCCA')

# print(test.validateSeq())
print(test2.validateSeq())

print(test2.countNucFrequency())

print(test2.show_seq_info())

print(test2.transcription())

print(test2.reverse_complement())
