# Transcribing DNA into RNA
f = open("data/rosalind_rna.txt", "r")
t = f.read()
# print t
'''
for i in range (0, len(t)-1):
	if t[i]=="T":
		t = t[:i] + "U" + t[i+1:]
print t
'''
u = t.replace("T","U")
print u
