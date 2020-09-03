import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('ouput.txt', 'w')

s = input()
t = input()
minCount = len(t)
i = 0
while i < len(s) and i + len(t) <= len(s):
    countSame = 0
    j = 0
    while j < len(t):
        if t[j] == s[i+j]:
            countSame += 1
        j += 1
        minCount = min(len(t) - countSame, minCount)
    i += 1
print(minCount)