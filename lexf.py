# Enumerating k-mers lexicographically

f = open("data/rosalind_lexf.txt", "r").read().splitlines()

A = f[0].split()
n = int(f[1])

words = []
words.append(A)

for i in range(n-1):
	words.append([])
	for j in words[i]:
		for k in A:
			words[i+1].append(j + k)
			words[i] = []
print "\n".join(words[-1])
