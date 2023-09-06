import string
alphabet = list(string.ascii_uppercase)
alphabet.insert(0, ".")
H, W = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]
for i in range(H):
  rslt = ""
  for j in range(W):
    rslt += alphabet[S[i][j]]
  print(rslt)