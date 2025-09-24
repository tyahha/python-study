t = int(input())
n = int(input())
aa = [0] * (t + 1)
for _ in range(n):
    [l, r] = list(map(int, input().split()))
    aa[l] += 1
    aa[r] -= 1
count = 0;
for i in range(t):
    count += aa[i]
    print(count)
