from DNAToolkit import *
import random
rndDNAStr = ''.join((random.choice(Nuclotides)
                     for nuc in range(100)))
rndDNAStr = validateSeq(rndDNAStr)
print(countNuclotideFrequencey(rndDNAStr))
