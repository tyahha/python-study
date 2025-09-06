import numpy as np

A = np.array([
  [1, 2],
  [3, 4],
])

B = np.array([
  [3, 0],
  [0, 6],
])

print(A * 10)
print(A * B)

# ブロードキャスト
C = [10, 20]
print(A * C)