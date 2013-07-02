# Downloading from GenBank with Entrez

from Bio import Entrez

criteria = open("data/rosalind_gbk.txt", "r").read().split()

genus = criteria[0]
start_date = criteria[1]
end_date = criteria[2]

Entrez.email = "fionnf@maths.tcd.ie"

handle = Entrez.esearch(db="nucleotide", term='"' + genus + '"' + '[Organism] AND ("' + start_date + '"[PDAT] : "' + end_date + '"[PDAT])')


record = Entrez.read(handle)
count = record["Count"]
print count
