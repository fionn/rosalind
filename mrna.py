# Inferring mRNA from Protein

protein = open("data/rosalind_mrna.txt", "r").read().strip()

from Bio.Data import CodonTable

codondict = {}

for codon, aa in CodonTable.unambiguous_dna_by_id[1].forward_table.viewitems():
	codondict[codon] = aa

#for codon in CodonTable.unambiguous_dna_by_id[1].stop_codons:
#	codondict[codon] = "0"

def frequency():
	f = {}
	for codon, aa in codondict.items():
		if not aa in f:
			f[aa] = 0
		f[aa] += 1
	return f

total = 3	# There are 3 stop codons.

for i in protein:
	total *= frequency()[i] 
	total %= int(1e6)

print total

