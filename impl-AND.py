# impl AND
import numpy as np

def AND(x1, x2):
  w1, w2, b = 0.5, 0.5, -0.7
  x = np.array([x1,x2])
  y = np.array([w1,w2])
  tmp = np.sum(x * y) + b
  if tmp <= 0:
    return 0
  else:
    return 1
  