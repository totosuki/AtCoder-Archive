N,A,B = map(int,input().split())
x = 0
for i in range(N):
  s,d = input().split()
  d = int(d)
  if A <= d <= B:
    if s == "East":
      x += d
    else:
      x -= d
  elif d < A:
    if s == "East":
      x += A
    else:
      x -= A
  else:
    if s == "East":
      x += B
    else:
      x -= B
if x > 0:
  print(f"East {x}")
elif x == 0:
  print(0)
else:
  print(f"West {abs(x)}")