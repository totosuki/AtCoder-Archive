N = input()
a = 0

for n in N:
  a += int(n)

if not int(N) % a:
  print("Yes")
else:
  print("No")