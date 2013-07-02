# Finding a shared motif
f = open("data/rosalind_lcs.txt", "r")
data = sorted(f.read().splitlines(), key = len)

cs = [""]
for block in xrange(len(data[0]) + 1, 0, -1):
	for a in xrange(len(data[0]) - block + 1):
		b = a + block
		match = True
		for string in data[1:]:
			if (data[0][a:b] not in string):
				match = False
				break
		if (match and len(data[0][a:b]) > len(cs[-1])):
			cs.append(data[0][a:b])
			lcs = data[0][a:b]
			break
print lcs
