N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))
l  = [i for i in range(N) if C[i] == T]
if not l:
  l = [i for i in range(N) if C[i] == C[0]]
new_R = [R[i] for i in l]
rslt = R.index(max(new_R))
print(rslt + 1)