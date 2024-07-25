X = {"ABC","ARC","AGC","AHC"}
S = set()
for i in range(3):
  S.add(input())
print(*(X-S))