# Find the most frequent k-mers in a string.

f = open("data/rosalind_1a.txt", "r").read().splitlines()

genome = str(f[0])
k = int(f[1])

def frequentkmers(text, k):
    frequency = {}
    for i in range(len(text) - k + 1):
        key = [text[i:i + k]][0]
        # frequency[key] = frequency.get(key, 0) + 1
        if key in frequency:
            frequency[key] += 1
        else:
            frequency[key] = 1

    for kmer, count in frequency.items():
        if count != max(frequency.values()):
            del frequency[kmer]
    return frequency

for kmer in frequentkmers(genome, k):
    print kmer, 



'''
# Inefficient, O(|genome|^2 * k).

kmer = []
countmax = 0

for i in range(len(genome) - k + 1):
    count = 0
    for j in range(len(genome) - k + 1):
        if (genome[i:i + k] == genome[j:j + k]):
            count += 1
            if (count == countmax and genome[i:i + k] not in kmer):
                kmer.append(genome[i:i + k])
            elif (count > countmax):
                countmax = count
                kmer = []
                kmer.append(genome[i:i + k])

for string in kmer:
    print string, 
'''

