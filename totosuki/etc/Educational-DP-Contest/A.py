N = int(input())
H = list(map(int, input().split()))

def dynamic_programming_get(l, N):
  l = [0, abs(l[0] - l[1])] + [0] * (N-2)
  for i in range(2, N):
    bf_1 = l[i-1] + abs(H[i-1] - H[i])
    bf_2 = l[i-2] + abs(H[i-2] - H[i])
    l[i] = min([bf_1, bf_2])
  return l

def dynamic_programming_send(l, N):
  l = [10**5] * (N)
  l[0] = 0
  for i in range(N-1):
    if i+1 < N:
      l[i+1] = min([l[i+1], l[i] + abs(H[i] - H[i+1])])
    if i+2 < N:
      l[i+2] = min([l[i+2], l[i] + abs(H[i] - H[i+2])])
  return l

# l = dynamic_programming_get(H, N)
l = dynamic_programming_send(H, N)
print(l[N-1])