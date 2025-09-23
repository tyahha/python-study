d = int(input())
n = int(input())
aa = [0] * (d + 1)
lrs = [list(map(int, input().split())) for _ in range(n)]
for l, r in lrs:
    aa[l - 1] += 1
    aa[r] -= 1
count = 0;
for i in range(1, d+1):
    count += aa[i - 1]
    print(count)
