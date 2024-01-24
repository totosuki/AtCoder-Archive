S = list(input())
N = int(input())
for i in range(N):
  l,r = map(int,input().split())
  x = S[l-1:r]
  x.reverse()
  S[l-1:r] = []
  S[l-1:l-1] = x
print("".join(S))