S, T, X = map(int, input().split())
if S < T:
  if S <= X < T:
    print("Yes")
  else:
    print("No")
else:
  if S <= X or X < T:
    print("Yes")
  else:
    print("No")