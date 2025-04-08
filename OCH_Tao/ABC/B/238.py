N = int(input())
A = list(map(int,input().split()))
L = [0]
for i in range(N):
  L.append((L[-1]+A[i])%360)
else:
  L.append(360)
  L.sort(reverse=True)
print(max([L[i]-L[i+1] for i in range(N+1)]))