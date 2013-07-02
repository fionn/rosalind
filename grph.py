# Overlay graphs
f = open("data/rosalind_grph.txt", "r")
data = f.read().split(">")
del data[0]

k, dna = 3, []

for i in range(len(data)):
	dna.append("".join(data[i].splitlines()[1:]))

for i in range(len(dna)):
	for j in range(len(dna)):
		if (i != j and dna[i][-k:] == dna[j][:k]):
			print data[i].splitlines()[0], data[j].splitlines()[0]
