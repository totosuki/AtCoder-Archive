a = int(input())
b = int(input())
up = dn = 0

if a < b:
  up = b - a
  dn = a + (10-b)
else:
  up = (10-a) + b
  dn = a - b

print(up) if up < dn else print(dn)
# up = (b-a) if a < b else (a+b)
# dn = ((b-a)) if a < b else