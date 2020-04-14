# uses memoization with dictionaries to store base cases
from typing import Dict
memo: Dict[int, int] = { 0: 0, 1: 1 }

def fib2(n: int):
  if (n not in memo):
    memo[n] = fib2(n - 1) + fib2(n - 2)
  return memo[n]

print(fib2(80))
