# Find the most frequent k-mers with mismatches and reverse compliments
# in a string.

f = open("data/rosalind_1h.txt", "r").read().split()

genome = f[0]
k, d = int(f[1]), int(f[2])

def variants(string):
    setofstring = {string}
    return recursivemismatch(setofstring, d, 0)

def recursivemismatch(setofstrings, d, depth):
    if depth < d:
        localset = set()
        for string in setofstrings:
            for i in range(len(string)):
                for nt in {"A", "T", "G", "C"}:
                    temp = list(string)
                    temp[i] = nt
                    mismatch.add("".join(temp))
                    localset.add("".join(temp))
        return recursivemismatch(localset, d, depth + 1)
    return 0

def revc(s):
    s = s[::-1]
    s = s.replace("A", "t").replace("T", "a").replace("C", "g").replace("G", "c")
    return s.upper()

frequency, bucket, t = {}, set(), 0

for i in range(len(genome) - k + 1):
    mismatch = set()
    variants(genome[i:i + k])
    for kmer in mismatch:
        frequency[kmer] = frequency.get(kmer, 0) + 1
        frequency[revc(kmer)] = frequency.get(revc(kmer), 0)

for kmer in frequency:
    if frequency[kmer] + frequency[revc(kmer)] > t:
        bucket = {kmer}
        t = frequency[kmer] + frequency[revc(kmer)]
    elif frequency[kmer] + frequency[revc(kmer)] == t:
        bucket.add(kmer)
    
print " ".join(bucket)

