# Counting point mutations
f = open("data/rosalind_hamm.txt", "r")
data = f.read().splitlines()
d_H = 0

for i in range(len(data[0])):
	if (data[0][i] != data[1][i]):
		d_H += 1

print d_H
