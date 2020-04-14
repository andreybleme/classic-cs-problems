# first and most simple: performs too many function calls
def fib1(n: int):
  if (n < 2):
    return n
  return fib1(n - 1) + fib1(n - 2)

print(fib1(8))