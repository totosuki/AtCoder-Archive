H, W = map(int, input().split())
C = [input() for _ in range(H)]
rslt = []

for i in range(H):
  rslt.append(C[i])
  rslt.append(C[i])

[print("".join(r)) for r in rslt]