N = int(input())
S = input()
l = []
for i in range(50):
  if i == 0:
    l.append("b")
  elif i%3 == 1:
    l.append(f"a{l[-1]}c")
  elif i%3 == 2:
    l.append(f"c{l[-1]}a")
  else:
    l.append(f"b{l[-1]}b")
if S in l:
  print(l.index(S))
else:
  print(-1)