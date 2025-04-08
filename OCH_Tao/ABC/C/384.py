L = list(map(int, input().split()))
S = "ABCDE"
D = []
for i in range(1, 1 << 5):
  X = ""
  cnt = 0
  for j in range(5):
    if (i // (1 << j)) % 2 == 1:
      X += S[j]
      cnt += L[j]
  D.append({"cnt": cnt, "X": X})
D.sort(key=lambda x: (-x["cnt"], x["X"]))
for i in D:
  print(i["X"])
