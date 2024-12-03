import csv

left = []
right = []

with open(file=r"C:\PythonLearning\AOC\day1-part1-input.txt") as file:
        reader = csv.reader(file, delimiter=" ")
        for r in reader:
                left.append(int(r[0]))
                right.append(int(r[3]))

sum = 0
c = 0

for l in left:
        c = right.count(l)
        sum += l * c
        c = 0

print(sum)