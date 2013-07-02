# dna.py with Biopython

from Bio.Seq import Seq

dna = open("data/rosalind_ini.txt", "r").read()

s = Seq(dna)

print s.count("A"), s.count("C"), s.count("G"), s.count("T")
