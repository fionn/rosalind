# Find all approximate occurrences of a pattern in a string.

data = open("data/rosalind_1f.txt", "r").read().splitlines()

pattern, genome = data[0], data[1]
d = int(data[2])
L = len(pattern)

def distance(string1, string2):
    d_H = 0

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            d_H += 1
    return d_H

for i in range(len(genome) - L + 1):
    if distance(pattern, genome[i:i + L]) <= d:
        print i,

