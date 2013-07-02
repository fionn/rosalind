# Enumerating gene orders
f = open("data/rosalind_perm.txt", "r")
n = int(f.readline().strip())

factorial = 1
for i in range(1,n+1):
	factorial *= i
print factorial

def permute(a,k=0):	# [stackoverflow.com/a/11962517]
	if(k==len(a)):
		print " ".join(map(str, a))
	else:
		for i in xrange(k,len(a)):
			# print "i =", i, "k =", k, a, "(1)"
			a[k],a[i] = a[i],a[k]
			permute(a, k+1)
			# print "i =", i, "k =", k, a, "-->",
			a[k],a[i] = a[i],a[k]
			# print a

permute(range(1,n+1))
