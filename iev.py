# Calculating expected offspring

frequency = open("data/rosalind_iev.txt", "r").read().split()
x = [1, 1, 1, 0.75, 0.5, 0]

E = 0

for i in range(len(x)):
	E += int(frequency[i]) * x[i]

print 2 * E
