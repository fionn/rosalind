# Complementing a strand of DNA
f = open("data/rosalind_revc.txt", "r")
s = f.read()
r = s[::-1]
# print r
'''
r = r + "X"
for i in range (len(r)):
	if r[i] == "A":
		r = r[:i] + "T" + r[i+1:]
		print i, "A -> T"
		i+=1
	if r[i] == "T":
		r = r[:i] + "A" + r[i+1:]
		print i, "T -> A"
		i+=1
	if r[i] == "C":
		r = r[:i] + "G" + r[i+1:]
		print i, "C -> G"
		i+=1
	if r[i] == "G":
		r = r[:i] + "X" + r[i+1:]
		print i, "G -> C"
		i+=1
		print i
r = r[:-1]
'''
r = r.replace("A","t").replace("T","a").replace("C","g").replace("G","c")
r = r.replace("t","T").replace("a","A").replace("g","G").replace("c","C")
print r
