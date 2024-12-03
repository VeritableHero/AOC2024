import csv

sort1 = []
sort2 = []

with open(file=r"C:\Users\csmith\OneDrive - clarkinc.biz\Desktop\AOC\day1-part1-input.txt") as file:
        reader = csv.reader(file, delimiter=" ")
        for r in reader:
                sort1.append(int(r[0]))
                sort2.append(int(r[3]))

sort1.sort()
sort2.sort()
sum = 0
c = 0

for s in sort1:
        sum += abs(s - sort2[c])
        c += 1

print(sum)