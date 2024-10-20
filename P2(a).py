def F(n):
  if n <= 0:
    return "Invalid input. N must be greater than 0."
  elif n == 1:
    return 0
  elif n == 2:
    return 1
  else:
    return F(n-1) + F(n-2)

n = int(input("Enter a value for N (N > 0): "))
result = F(n)
print(f"The {n}th Fibonacci number is: {result}")