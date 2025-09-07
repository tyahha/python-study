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
OR = gateConstructor(0.5,0.5,-0.2)
NAND = gateConstructor(-0.1,-0.1,0.2)

def XOR(x1,x2):
  s1 = OR(x1,x2)
  s2 = NAND(x1,x2)
  return AND(s1,s2)
