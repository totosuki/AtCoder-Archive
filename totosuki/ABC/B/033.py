N = int(input())
L = [input().split() for _ in range(N)]

p_sum = sum([int(l[1]) for l in L])

for i in range(N):
  if int(L[i][1]) * 2 > p_sum:
    print(L[i][0])
    exit()

print("atcoder")