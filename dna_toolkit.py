nucleotides = ['A', 'C', 'G', 'T']


def validateSeq(dna_seq):
    temsep = dna_seq.Upper()
    for nuc in temsep:
        if nuc not in nucleotides:
            return False
        return temsep
