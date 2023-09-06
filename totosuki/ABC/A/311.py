N = int(input())
S = input()
se = set()

for i in range(len(S)):
  se.add(S[i])
  if len(se) == 3:
    print(i+1)
    exit()