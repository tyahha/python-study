input()

aa = list(map(int, input().split(" ")))

q = int(input())

sums = [[0,0]]
wins = 0
looses = 0
for a in aa:
  if a == 1:
    wins += 1
  else:
    looses += 1
  sums.append([wins, looses])

for i in range(q):
  l, r = map(int, input().split(" "))
  pw, pl = sums[r]
  qw, ql = sums[l-1]
  wins = pw - qw
  looses = pl - ql
  if wins > looses:
    print("win")
  elif wins < looses:
    print("lose")
  else:
    print("draw")