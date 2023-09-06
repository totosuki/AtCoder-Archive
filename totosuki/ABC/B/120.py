A, B, K = map(int, input().split())
check_range = min([A, B])
l = []
for num in range(1, check_range + 1):
  if (A % num == 0) and (B % num == 0):
    l.append(num)
print(l[-K])