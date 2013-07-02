# Independent alleles

f = open("data/rosalind_lia.txt", "r").read().split()

k, N = int(f[0]), int(f[1])

def factorial(n):
	if (n == 0):
		return 1
	else:
		return n * factorial(n - 1)

def binomial(n, k):
	return factorial(n) / (factorial(k)*factorial(n-k))

def pmf(k, n, p):
	return binomial(n, k) * (p**k) * ((1 - p) ** (n - k))	

P = 0
for i in range(N, 2**k + 1):
	P += pmf(i, 2**k, 0.25)

print P

