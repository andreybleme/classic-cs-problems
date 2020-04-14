def calculate_pi(terms: int):
  numerator: float = 4.0
  denominator: float = 1.0
  pi: float = 0.0
  operation: float = 1.0

  for _ in range(terms):
    pi += operation * (numerator / denominator)
    denominator += 2.0
    operation *= -1.0
  return pi

if __name__ == "__main__":
  print(calculate_pi(100))