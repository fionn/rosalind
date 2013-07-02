# Calculating protein mass

protein = open("data/rosalind_prtm.txt", "r").read().strip()

masstable = dict((line.strip().split("   ") for line in file("data/monoisotopicmasstable.txt")))

mass = 0

for acid in protein:
	mass += float(masstable[acid])

print mass
