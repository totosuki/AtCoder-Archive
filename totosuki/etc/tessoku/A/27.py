A, B = map(int, input().split())

def GCD(a: int, b: int) -> int:
  if a < b:
    return GCD(b, a)
  else:
    if b == 0:
      return a
    else:
      return GCD(b, a % b)

print(GCD(A, B))