A, B, C, D = map(int, input().split())

if B <= C or A >= D:
  rslt = 0
else:
  rslt = min(B, D) - max(A, C)

print(rslt)