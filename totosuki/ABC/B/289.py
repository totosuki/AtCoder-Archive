N, M = map(int, input().split())
A = list(map(int, input().split()))
reverse_list = [False for _ in range(N)]
nums = list(range(1,N+1))
L = []
rslt = []

for i in range(len(A)):
  reverse_list[A[i]-1] = True

i = 0
while True:
  if i >= len(reverse_list):
    break
  l = []

  while reverse_list[i]:
    l.append(nums[i])
    i += 1
    if i >= len(reverse_list):
      break

  if not l:
    l.append(nums[i])
    i += 1
  else:
    l.append(nums[i])
    i += 1
  L.append(l)

for row in range(len(L)):
  for col in reversed(range(len(L[row]))):
    rslt.append(L[row][col])
print(*rslt)