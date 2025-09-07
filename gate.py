# impl AND
import numpy as np

def gateConstructor(w1,w2,b):
  def gate(x1,x2):
    x = np.array([x1,x2])
    y = np.array([w1,w2])
    tmp = np.sum(x * y) + b
    if tmp <= 0:
      return 0
    else:
      return 1
  return gate

AND = gateConstructor(0.5, 0.5, -0.7)