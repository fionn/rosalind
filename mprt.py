# Finding a protein motif

from Bio import SeqIO
import urllib2
import os

def motif(s, p):
	if s[p] == "N" and s[p+1] != "P" and (s[p+2] == "S" or s[p+2] == "T") and s[p+3] != "P":
		return True
	return False

uniprot_id = open("data/rosalind_mprt.txt", "r").read().splitlines()

f = open("mprttemp.fasta", "w")

for id in range(len(uniprot_id)):
	f.write(urllib2.urlopen("http://www.uniprot.org/uniprot/" + uniprot_id[id] + ".fasta").read())

f.close()

location, j = [], 0

for record in SeqIO.parse("mprttemp.fasta", "fasta"):
	location.append([])
	for i in range(len(record.seq) - 4):
		if motif(record.seq, i):
			location[j].append(i + 1)
	j += 1

for i in range(len(uniprot_id)):
	if location[i] != []:
		print uniprot_id[i]
		for k in location[i]:
			print k,
		print ""

os.remove("mprttemp.fasta")
