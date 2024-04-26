N = int(input())
P = []
for i in range(N):
  P.append(int(input()))
print(sum(P)-max(P)//2)