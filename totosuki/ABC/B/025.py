N, A, B = map(int, input().split())
pos = 0

for i in range(N):
  s, d = input().split()
  d = int(d)

  if d < A:
    d = A
  elif d > B:
    d = B
  
  if s == "East":
    pos += d
  else:
    pos -= d

if pos > 0:
  print("East", pos)
elif pos < 0:
  print("West", abs(pos))
else:
  print(0)