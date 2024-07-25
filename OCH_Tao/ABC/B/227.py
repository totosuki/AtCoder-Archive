N = int(input())
S = list(map(int,input().split()))
X = set()
for a in range(1,1001):
  for b in range(1,1001):
    X.add(4*a*b+3*a+3*b)
print(len([i for i in S if i not in X]))