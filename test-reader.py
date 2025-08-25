def putfile(file):
  with open(file) as f:
    lines = f.readlines()
    print(lines)

if __name__ == '__main__':
  import sys
  putfile(sys.argv[1])
