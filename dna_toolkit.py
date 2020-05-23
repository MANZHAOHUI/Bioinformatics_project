nucleotides = ['A', 'C', 'G', 'T']


def validateSeq(dna_seq):
    temsep = dna_seq.upper()
    for nuc in temsep:
        if nuc not in nucleotides:
            return False
    return temsep
