f = open("data/rosalind_ini5.txt", "r")
a = f.readlines()

f = open("data/ini5out.txt", "w")

for i in range(0,len(a)):
	if (i+1)%2==0:
		line = str(a[i])
		f.write(line)
f.close()
