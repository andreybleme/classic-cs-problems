# traditional without recursion
def fib4(n: int):
  if (n == 0):
    return 0
  
  last: int = 0
  next: int = 1
  
  for _ in range(1, n):
    temp = last
    last = next
    next = temp + next
    # could also use tuple unpacking to avoid using the 'temp' variable
    # last, next = next, last + next
  return next

print(fib4(8))
