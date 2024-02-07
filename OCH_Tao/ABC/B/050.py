N = int(input())
T = list(map(int,input().split()))
M = int(input())
l = []
for i in range(M):
  p,x = map(int,input().split())
  l.append(sum(T)-T[p-1]+x)
print("\n".join(str(i) for i in l))