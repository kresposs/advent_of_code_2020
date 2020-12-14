with open("C:\\Users\\marco\\OneDrive\\Programmazione\\Advent of Code 2020\\Day 3\\input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

lineLenght = len(lines[0])

trees = 0
count = 0

for i in lines:
    if i[(3*count) % lineLenght] == "#":
        trees = trees + 1
    count = count + 1
print(trees)