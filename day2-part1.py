import csv

raw = []
filtered = []

rows = 0

with open(file=r"D:\AdventOfCode\day2-input.txt") as file:
        reader = csv.reader(file, delimiter=" ")
        for r in reader:
                raw.append([int(x) for x in r])

for r in raw:
        if (r == sorted(r)):
                filtered.append(r)
        if (r == sorted(r, reverse=True)):
                filtered.append(r)

for f in filtered:
        differences = [abs(f[x] - f[x+1]) for x in range(len(f)-1)]
        item_min = min(differences)
        item_max = max(differences)
        if item_min > 0 and item_max < 4:
                rows += 1
                # print(f) # spot check results


print(rows)