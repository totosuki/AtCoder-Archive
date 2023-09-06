N, X = map(int, input().split())
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rslt = ""
for t in alphabet:
  rslt += t * N

print(rslt[X-1])