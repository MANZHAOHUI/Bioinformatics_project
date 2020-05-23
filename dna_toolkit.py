nucleotides = ['A', 'C', 'G', 'T']


def validateSeq(dna_seq):
    temsep = dna_seq.upper()
    for nuc in temsep:
        if nuc not in nucleotides:
            return False
    return temsep


def countNucFrequency(seq):
    temFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nuc in seq:
        temFreqDict[nuc] += 1
    return temFreqDict
