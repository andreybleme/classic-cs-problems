# generating fibonacci numbers using yield
from typing import Generator

def fib5(n: int):
  yield 0
  if (n > 0):
    yield 1
  
  last: int = 0
  next: int = 1
  
  for _ in range(1, n):
    last, next = next, last + next
    yield next

for i in fib5(8):
  print('Fib5: ', i)
  