# Fibonacci Rabbits

nk = open("data/rosalind_fib.txt", "r").readline().split()

def genfib(n, k):
	if (n == 1 or n == 2):
		return 1
	elif (n==0):
		pass
	else:
		return genfib(n - 1, k) + k * genfib(n - 2, k)

def fiblight(n, k):
	f1, f2 = 1, 1
	for i in range(2, n):
		f1, f2 = f2, k * f1 + f2
	return f2

n, k = int(nk[0]), int(nk[1])

#print genfib(n, k),

print fiblight(n, k)
