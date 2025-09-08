import numpy as np
import matplotlib.pylab as plt

def f(x):
  return x ** 2 + 3 * x + 1

def main():
  x = np.arange(-10,10,0.1)
  y = f(x)
  plt.plot(x,y)
  plt.ylim(-10,10)
  plt.show()

if __name__ == "__main__":
  main()