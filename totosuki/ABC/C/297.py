import sys
input = sys.stdin.buffer.readline

H, W = map(int, input().split())

for _ in range(H):
  S = list(input().decode().rstrip())
  j = 0
  while j < W-1:
    if S[j] == "T" and S[j+1] == "T":
      S[j] = "P"
      S[j+1] = "C"
      j += 2
    else:
      j += 1
  print("".join(S))