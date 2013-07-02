#Computing GC content
f = open("data/rosalind_gc.txt", "r")
data = f.read().split(">")
del data[0]

gc, strand, gcarray = [], [], []
index, biggestgc = 0, 0

for i in range(len(data)):
	
	strand.append("".join(data[i].splitlines()[1:]))
	
	gc.append(strand[i].count("G") + strand[i].count("C"))
	
	gcarray.append(100 * float(gc[i]) / len(strand[i]))

	if (gcarray[i] > biggestgc):
		index = i
		biggestgc = gcarray[i]

print str(data[index].splitlines()[0])+"\n"+ str(gcarray[index]) + "%"
