ss = input()
n = 0
e = 1
for c in reversed(ss):
    if c == "1":
        n += e
    e *= 2
print(n)