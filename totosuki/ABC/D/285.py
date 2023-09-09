import sys; from collections import defaultdict
input = sys.stdin.buffer.readline

N = int(input())
g = defaultdict(str)
answer = "Yes"

for _ in range(N):
  S, T = input().decode().rstrip().split()
  g[S] = T

k_list = {k:False for k in g.keys()}

for k in k_list:
  if k_list[k]:
    continue
  
  se = set()
  se.add(k)
  next = g[k]
  safe = True

  while g[next]:
    if next in se:
      safe = False
      break

    if k_list[next]:
      break
    
    se.add(next)
    k = next
    next = g[k]
  
  if safe:
    for t in se:
      k_list[t] = True
  else:
    answer = "No"
    break

print(answer)