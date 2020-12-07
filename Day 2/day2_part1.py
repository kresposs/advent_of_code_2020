"""
--- Day 2: Password Philosophy ---
Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via toboggan.

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of passwords (according to the corrupted database) and the corporate policy when that password was set.


"""

with open("C:\\[pippo]\\[pippo]\\[pippo]\\[pippo]\\Advent of Code 2020\\Day 2\\passwords.txt") as f:
    pwdFile = f.read()

pwdFileList = pwdFile.split("\n")

counter = 0
finePwd = 0

for i in range(len(pwdFileList)):
    txt = pwdFileList[i]   
    txt = txt.split(" ")
    tmp = txt[0].split("-")
    min = int(tmp[0])
    max = int(tmp[1])
    digit = txt[1].split(":")
    digit = digit[0]
    for i in range(len(txt[2])):
        if digit in txt[2][i]:
            counter = counter + 1
    if counter >= min and counter <= max:
        finePwd = finePwd + 1
    counter = 0


print(finePwd)  

