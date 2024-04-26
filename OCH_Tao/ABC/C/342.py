N = int(input())
S = input()
Q = int(input())
for i in range(Q):
  C,D = input().split()
  S = S.replace(C,D)
print(S)