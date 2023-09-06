C = [list(input().split()) for _ in range(4)]
C = [C[i][j] for i in [3,2,1,0] for j in [3,2,1,0]]
C = [C[i:i+4] for i in range(0, len(C), 4)]
for c in C:
  print(*c)