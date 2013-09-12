# RNA splicing

from Bio.Seq import Seq
from Bio.Alphabet import generic_rna

data = open("data/rosalind_splc.txt", "r").read().split(">")
del data[0]

dna = "".join(data[0].splitlines()[1:])

introns = []

for i in range(1, len(data)):
	introns.append("".join(data[i].splitlines()[1:]))

for i in range(len(introns)):
	dna = dna.replace(introns[i], "")

rna = dna.replace("T", "U")

protein = Seq(rna, generic_rna).translate(to_stop = True)

print protein

