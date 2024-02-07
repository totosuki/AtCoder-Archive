def fx(x):
  return x**2 + 2*x + 3
t = int(input())
print(fx(fx(fx(t)+t)+fx(fx(t))))