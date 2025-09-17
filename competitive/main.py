n = int(input())
val = ""
while n != 0:
  val += "0" if n % 2 == 0 else "1"
  n //= 2
val += "0" * 10
print(val[::-1][-10:])
