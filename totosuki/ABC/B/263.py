N = int(input())
P = list(map(int, input().split()))
rslt = [0] * N
for i in range(len(P)):
  rslt[i+1] = rslt[P[i]-1] + 1
print(rslt[-1])