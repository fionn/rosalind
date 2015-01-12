# Complementing a strand of DNA

s = open("data/rosalind_1b.txt", "r").read().strip()

r = s[::-1]

r = r.replace("A","t").replace("T","a").replace("C","g").replace("G","c")
r = r.upper()

print r

