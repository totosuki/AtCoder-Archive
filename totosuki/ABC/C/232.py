from itertools import*
N,M=map(int,input().split())
T=[list(map(int,input().split()))for _ in[0]*M]
A,r=[list(map(int,input().split()))for _ in[0]*M],"No"
for p in permutations(range(1,N+1)):
  if all([sorted([p[T[i][0]-1],p[T[i][1]-1]])in A for i in range(M)]):r="Yes"
print(r)