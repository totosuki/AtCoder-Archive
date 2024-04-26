import collections
N = int(input())
S = input()
D = collections.Counter(S)
if D["T"]==D["A"]:
  print("T" if S.rindex("T")<S.rindex("A") else "A")
else:
  print(max(D,key=D.get))