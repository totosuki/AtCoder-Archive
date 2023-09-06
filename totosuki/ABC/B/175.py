from itertools import combinations
N = int(input())
L = list(map(int, input().split()))
cnt = 0

for combo in combinations(range(N), 3):
  i, j, k = combo
  tmp = sorted([L[i], L[j], L[k]])
  
  if L[i] == L[j] or L[j] == L[k] or L[k] == L[i]: continue
  if not tmp[2] < (tmp[0] + tmp[1]): continue
  
  cnt += 1

print(cnt)