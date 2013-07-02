# Mortal Fibbonacci Rabbits

nm = open("data/rosalind_fibd.txt", "r").readline().split()

n, m = int(nm[0]), int(nm[1])

#n, m = 6, 3

k = 1 	# age of fertility

f = [0,1,1] 

for i in range(3, n + 2):
	s = 0
	for j in range(i - m, i - (k + 1) + 1):
		if j > 0:
			s += f[j]
		#print i, j 
	f.append(s)

print f[-1]
