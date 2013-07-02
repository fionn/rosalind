# Getting data from UniProt with RegEx

import urllib2
import re

uniprot_id = open("data/rosalind_dbpr.txt", "r").read().strip()
data = urllib2.urlopen("http://www.uniprot.org/uniprot/" + uniprot_id + ".txt").read()

print '\n'.join(line.group(1) for line in re.finditer("P:([a-zA-Z ]*)", data))
