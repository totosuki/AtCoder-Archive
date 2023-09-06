N, Y = map(int, input().split())
collect = False

for i in range(N + 1):
  for j in range((N - i) + 1):
    total = (i*10000) + (j*5000) + ((N-i-j)*1000)
    if (i + j + (N - i - j)) == N and total == Y:
      print(f"{i} {j} {N - i - j}")
      collect = True
      break
  if collect:
    break
if not collect:
  print("-1 -1 -1")