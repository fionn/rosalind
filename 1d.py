# Find patterns forming clumps in a string. O(n).

f = open("data/rosalind_1d.txt", "r").read().splitlines()

genome = f[0]
f[1] = f[1].split(" ")
k, L, t = int(f[1][0]), int(f[1][1]), int(f[1][2])

frequency, bucket = {}, set()

# This covers the first L nucleotides.
for i in range(L - k + 1):
    key = [genome[i:i + k]][0]
    frequency[key] = frequency.get(key, 0) + 1
    if frequency[key] >= t:
        bucket.add(key)

# This just deals with the edges of the window.
for n in xrange(1, len(genome) - L + 1):
    tail = genome[n:n + k]
    head = genome[n + L - k:n + L]
    frequency[tail] -= 1
    frequency[head] = frequency.get(head, 0) + 1
    if frequency[head] >= t:
        bucket.add(head)

for kmer in bucket:
    print kmer,

