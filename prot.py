# Protein Translation
f = open("data/rosalind_prot.txt", "r")
rna = f.read().strip()
# print rna
f = open("data/mrnacodontable.txt", "r")
codex = f.read().replace("Stop", "0   ").replace("\n", "      ").split("      ")

for i in range(len(codex)):
	codex[i] = codex[i].replace("0", "Stop").split()
del codex[-1]

rnarray = []
while rna:
	rnarray.append(rna[:3])
	rna = rna[3:]

protein = rnarray
for i in range(len(codex)):
	for j in range(len(rnarray)):
		if (codex[i][0] == protein[j] and codex[i][1] != "Stop"):
			protein[j] = codex[i][1]
		if (codex[i][0] == protein[j] and codex[i][1] == "Stop"):
			del protein[j]
			break
print "".join(protein)
