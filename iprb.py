# Mendel's first law

f = open("data/rosalind_iprb.txt", "r")
data = f.read().split()

# k, m, n = float(data[0]), float(data[1]), float(data[2])

T = float(data[0]) + float(data[1]) + float(data[2])
a = 1 / (T*(T-1))
Pr = 0
P = [range(len(data)),range(len(data)),range(len(data))]
c = [[1]*len(data),[1]*len(data),[1]*len(data)]

c[1][1] = 0.75
c[1][2] = 0.5
c[2][1] = 0.5
c[2][2] = 0

for i in range(len(data)):
	for j in range (len(data)):
		P[i][j] = c[i][j] * a * int(data[i]) * int(data[j])
		P[i][i] = c[i][i] * a * int(data[i]) * (int(data[i]) - 1)
		Pr += P[i][j]

print Pr
