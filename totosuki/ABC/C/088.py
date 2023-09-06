import sys

c = []
for _ in range(3):
  c.append(list(map(int, input().split())))

A1 = list(range(min(c[0][:]) + 1))
A2 = list(range(min(c[1][:]) + 1))
A3 = list(range(min(c[2][:]) + 1))

for a1 in A1:
  for a2 in A2:
    for a3 in A3:
      if ((c[0][0] - a1 == c[1][0] - a2 == c[2][0] - a3)
        and (c[0][1] - a1 == c[1][1] - a2 == c[2][1] - a3)
        and (c[0][2] - a1 == c[1][2] - a2 == c[2][2] - a3)):
          print("Yes")
          sys.exit()
print("No")

# a1 = list(range(min(c[0][:]) + 1))
# a2 = list(range(min(c[1][:]) + 1))
# a3 = list(range(min(c[2][:]) + 1))
# b1 = list(range(min([row[0] for row in c]) + 1))
# b2 = list(range(min([row[1] for row in c]) + 1))
# b3 = list(range(min([row[2] for row in c]) + 1))
# A = [a1, a2, a3]
# B = [b1, b2, b3]