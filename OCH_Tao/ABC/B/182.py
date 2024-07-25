N = int(input())
A = list(map(int,input().split()))
ans = []
for i in range(2,1001):
  ans.append(len([j for j in A if j%i==0]))
print(ans.index(max(ans))+2)