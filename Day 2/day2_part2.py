"""
--- Part Two ---
While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two positions in the password, where 1 means the first character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) Exactly one of these positions must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

How many passwords are valid according to the new interpretation of the policies?
"""

with open("C:\\..\\passwords.txt") as f:
    pwdFile = f.readlines()

finePwd = 0

for i in range(len(pwdFile)):

    txt = pwdFile[i]   
    txt = txt.split(" ")
    tmp = txt[0].split("-")
    position1 = int(tmp[0])
    position2 = int(tmp[1])
    digit = txt[1].split(":")
    digit = digit[0]
    #txt[2] = "".join(["-", txt[2]])

    if (digit == txt[2][position1-1] and digit != txt[2][position2-1]) or (digit == txt[2][position2-1] and digit != txt[2][position1-1]):
        finePwd = finePwd + 1


print(finePwd)  

