S = input()
K = int(input())
l = []
if len(S)<K:
  print(0)
else:
  for i in range(len(S)):
    l.append(S[i:i+K])
  x = [i for i in l if len(i)==K]
  print(len(list(set(x))))