def GCD(a: int, b: int) -> int:
  if a < b:
    return GCD(b, a)
  else:
    if b == 0:
      return a
    else:
      return GCD(b, a % b)

A, B = map(int, input().split())
print((A*B) // GCD(A,B))