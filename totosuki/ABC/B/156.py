def f(n, k):
  amari = n % k

  if n // k == 0:
    return str(amari)
  
  return f(n // k, k) + str(amari)

N, K = map(int, input().split())
print(len(f(N, K)))