N = int(input())
K = int(input())
X = list(map(int,input().split()))
l = []
for i in X:
  l.append(2*(min(i,K-i)))
print(sum(l))