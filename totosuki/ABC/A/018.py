A = int(input())
B = int(input())
C = int(input())
ABC = [A, B, C]
rslt = sorted(ABC, reverse = True)
for i in range(3):
  print(rslt.index(ABC[i]) + 1)