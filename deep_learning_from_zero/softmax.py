import numpy as np

def softmax(a):
  max = np.max(a)
  a = a - max  # オーバーフロー対策
  exp_a = np.exp(a)
  sum_exp_a = np.sum(exp_a)
  y = exp_a / sum_exp_a
  return y