S = input()
T = input()
for s,t in zip(S,T):
  if s == t:
    continue
  elif (s == "@" or t == "@") and ((s in "@atcoder") and (t in "@atcoder")):
    continue
  else:
    print("You will lose")
    exit()
print("You can win")