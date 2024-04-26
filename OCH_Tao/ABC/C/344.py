N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
L = int(input())
C = list(map(int,input().split()))
Q = int(input())
X = list(map(int,input().split()))
L = ["No"]*Q
for i in A:
  for j in B:
    for k in C:
      if i+j+k in X:
        L[X.index(i+j+k)]="Yes"
print("\n".join(L))