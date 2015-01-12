# Find a position in a genome minimizing the skew. O(n).

genome = open("data/rosalind_1e.txt", "r").read().strip()

skew = 0
minimum, minima = 1, []

for i in range(len(genome)):
    # print genome[i],
    if genome[i] == "G":
        skew += 1
    elif genome[i] == "C":
        skew -= 1
    if skew < minimum:
        minimum = skew
        minima = [i + 1]
    elif skew == minimum:
        minima.append(i + 1)

print " ".join(map(str, minima))

