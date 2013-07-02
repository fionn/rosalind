# Python dictionaries.

data = open("data/rosalind_ini6.txt", "r").read().split()

d = {}

for word in data:
	if word in d:
		d[word] += 1
	else:
		d[word] = 1

for key, value in d.items():
	print key, value
