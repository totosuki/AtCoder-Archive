H, M = input().split()
H, M = H.zfill(2), M.zfill(2)
A, B, C, D = list(map(int, [H[0], H[1], M[0], M[1]]))

for a in range(3):
  if a < A: continue
  for b in range(10):
    if a == A and b < B: continue
    if a == 2 and b >= 4:
      continue
    for c in range(6):
      if a == A and b == B and c < C: continue
      for d in range(10):
        if a == A and B == B and c == C and d < D: continue
        if int(str(a)+str(c)) <= 23 and int(str(b)+str(d)) <= 59:
          print(int(str(a)+str(b)), int(str(c)+str(d)))
          exit()

print("0 0")