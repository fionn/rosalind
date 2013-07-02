# Counting DNA nucleotides
f = open("data/rosalind_dna.txt", "r")
s = f.read()
# print s
'''
a = 0
c = 0
g = 0
t = 0

for i in range(0, len(s)-1):
	if s[i]=="A":
		a+=1
	if s[i]=="C":
		c+=1
	if s[i]=="G":
		g+=1
	if s[i]=="T":
		t+=1

print str(a) + " " + str(c) + " " + str(g) + " " + str(t)
'''
# for i in "ACGT":
#	print s.count(i),
print s.count("A"), s.count("C"), s.count("G"), s.count("T")
