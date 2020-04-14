# uses automatic memoization with annotation
from functools import lru_cache

@lru_cache(maxsize=None)
def fib3(n: int):
  if (n < 2):
    return n

print(fib3(21))
