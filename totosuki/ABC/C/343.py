N = int(input())

cube = []
x = 1
while True:
  if x**3 > 10**18:
    break
  s = list(str(x**3))
  for i in range(len(s)//2):
    if s[i] != s[-i-1]:
      break
  else:
    cube.append(x**3)
  x += 1

ans = 1
for i in range(len(cube)):
  if cube[i] > N:
    break
  ans = cube[i]

print(ans)