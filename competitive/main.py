n, k = map(int, input().split())
aa = list(map(int, input().split()))

def check(x):
    count = 0
    for a in aa:
        count += x // a

    return count >= k

left, right = 1, min(aa) * k
while left < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid + 1
print(left)