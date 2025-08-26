import torch

def test():
  t = torch.tensor([[1,2], [3,4]])
  print(t)
  print(t.T)
  print(t)
  t = t.T
  print(t)
  print(t.T)

if __name__ == "__main__":
  test()