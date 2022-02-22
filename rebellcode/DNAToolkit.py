import collections
Nuclotides = ["A", "C", "G", "T"]


def validateSeq(dna_seq):
    tmseq = dna_seq.upper()
    for nuc in tmseq:
        if nuc not in Nuclotides:
            return False
    return tmseq


def countNuclotideFrequencey(seq):
    # tmFreqDict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    # for nuc in seq:
    #     tmFreqDict[nuc] += 1
    # return tmFreqDict
    return dict(collections.Counter(seq))


