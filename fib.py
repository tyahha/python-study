def fib2(n):
  """n までのフィボナッチ級数から成るリストを返す"""
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)
    a, b = b, a+b
  return result
