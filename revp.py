# Locating Restriction sites
s = open("data/rosalind_revp.txt", "r").read().strip()

def rc(string):
	r = string.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()[::-1]
	return r

# print s
# print rc(s)
# print "1234567890123456789012345 \t <--human"
# print "0123456789012345678901234 \t <--logic"

'''# Unordered, but probably faster
for block in range(12, 3, -1):
	for a in range(len(s) - block + 1):
		b = a + block
		if (s[a:b] == rc(s[a:b]) and s[a:b] in rc(s)):
			print a + 1, b - a
'''

for a in range(len(s)-3):
	for block in range(4, min(13, len(s) - a + 1), 2):
		b = a + block
		# print a + 1, b - a
		if (s[a:b] == rc(s[a:b]) and s[a:b] in rc(s)):
			# print s[a:b], s
			print a + 1, b - a

'''
# Check the difference between ordered and unordered output of revp.py
ordered = open("ordered.txt", "r").read().splitlines()
unordered = open("unordered.txt", "r").read().splitlines()

for i in range(len(unordered)):
	if (unordered[i] not in ordered):
		print unordered[i]
'''
