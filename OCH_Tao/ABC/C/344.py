N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))
Q = int(input())
X = list(map(int,input().split()))
S = set()
for i in A:
  for j in B:
    for k in C:
      S.add(i+j+k)
for i in X:
  if i in S:
    print("Yes")
  else:
    print("No")