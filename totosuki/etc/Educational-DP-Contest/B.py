N, K = map(int, input().split())
H = list(map(int, input().split()))

def dynamic_programming(H, N, K):
  #Preprocessing
  if K > N:
    K = N
  start_list = [0] * K
  for i in range(K):
    tmp = []
    if i == 0:
      continue
    else:
      start_list[i] = abs(H[0] - H[i])

  l = start_list + [0] * (N-K)
  
  #DP
  for i in range(K, N):
    tmp = []
    for j in range(1, K+1):
      diff = l[i-j] + abs(H[i] - H[i-j])
      tmp.append(diff)
    l[i] = min(tmp)
  
  return l

l = dynamic_programming(H, N, K)
print(l[N-1])