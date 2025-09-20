_, q = map(int, input().split(" "))

aa = list(map(int, input().split(" ")))
sums = []
sum = 0
for a in aa:
  sum += a
  sums.append(sum)

for i in range(q):
  l, r = map(int, input().split(" "))
  if l == 1:
    print(sums[r-1])
  else:
    print(sums[r-1] - sums[l-2])