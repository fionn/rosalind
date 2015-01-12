# Finding a motif in DNA
data = open("data/rosalind_1c.txt", "r").read().splitlines()

#for i in range(len(data)):
#	data[i] = data[i].strip()

pattern = data[0]
genome = data[1]

for i in range(len(genome) - len(pattern)):
	if genome[i:i + len(pattern)] == pattern:
		print i,

