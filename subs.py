# Finding a motif in DNA
f = open("data/rosalind_subs.txt", "r")
data = f.readlines()

for i in range(len(data)):
	data[i] = data[i].strip()

for i in range(len(data[0])-len(data[1])):
	if data[0][i:i + len(data[1])] == data[1]:
		print i+1,
