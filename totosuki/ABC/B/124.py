N = int(input())
H = list(map(int, input().split()))
rslt = [H[0]]

for i in range(1, N):
  if H[i] >= rslt[-1]:
    rslt.append(H[i])

print(len(rslt))