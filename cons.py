# Consensus and profile -- finding a most likely common ancestor

string = open("data/rosalind_cons.txt", "r").read().splitlines()

A, C, G, T = [], [], [], []
cons = []
dictionary = ["A", "C", "G", "T"]

for j in xrange(len(string[0])):
	a, c, g, t = 0, 0, 0, 0
	for i in range(len(string)):
		if (string[i][j] == "A"):
			a += 1
		if (string[i][j] == "C"):
			c += 1
		if (string[i][j] == "G"):
			g += 1
		if (string[i][j] == "T"):
			t += 1
	A.append(a)
	C.append(c)
	G.append(g)
	T.append(t)
	for nucleotide in [a, c, g, t]:
		if nucleotide == max(a, c, g, t):
			cons.append(dictionary[[a, c, g, t].index(nucleotide)])
			break

print "".join(map(str, cons))

print "A:", " ".join(map(str, A))
print "C:", " ".join(map(str, C)) 
print "G:", " ".join(map(str, G)) 
print "T:", " ".join(map(str, T))
