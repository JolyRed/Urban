def sum_three(a, b, c):
  """Складывает 3 числа."""
  return a + b + c

def is_prime(func):
  def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    if result <= 1:
      print("Составное")
    else:
      is_prime = True
      for i in range(2, int(result**0.5) + 1):
        if result % i == 0:
          is_prime = False
          break
      if is_prime:
        print("Простое")
      else:
        print("Составное")

  return wrapper

@is_prime
def sum_three(a, b, c):
  """Складывает 3 числа."""
  return a + b + c

result = sum_three(2, 3, 6)
print(result)  # Составное

