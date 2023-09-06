A, B, C = map(int, input().split())
if C - (A - B) < 0:
  print(0)
  exit()
print(C - (A - B))