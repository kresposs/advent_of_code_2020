with open("C:\\Users\\marco\\OneDrive\\Programmazione\\Advent of Code 2020\\Day 3\\input.txt") as f:
    lines = f.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].strip()

lineLenght = len(lines[0])

treesSlope1 = 0
treesSlope3 = 0
treesSlope5 = 0
treesSlope7 = 0
treesSlope1_down1 = 0
count = 0

for i in lines:
    if i[(1*count) % lineLenght] == "#":
        treesSlope1 = treesSlope1 + 1
    count = count + 1
#print(treesSlope1)

count = 0

for i in lines:
    if i[(3*count) % lineLenght] == "#":
        treesSlope3 = treesSlope3 + 1
    count = count + 1
#print(treesSlope3)

count = 0

for i in lines:
    if i[(5*count) % lineLenght] == "#":
        treesSlope5 = treesSlope5 + 1
    count = count + 1
#print(treesSlope5)

count = 0

for i in lines:
    if i[(7*count) % lineLenght] == "#":
        treesSlope7 = treesSlope7 + 1
    count = count + 1
#print(treesSlope7)

count = 0

for i in lines:
    if i[int(count / 2) % lineLenght] == "#" and count % 2 == 0:
        treesSlope1_down1 = treesSlope1_down1 + 1
    count = count + 1
#print(treesSlope1_down1)

totalTrees = (treesSlope1 * treesSlope3 * treesSlope5 * treesSlope7 * treesSlope1_down1)
print(totalTrees)