N, L = map(int, input().split())
data = [i for i in range(L, N+L)]
sum_data = sum(data)
min_i = min_abs = 10000000

for i in range(N):
  tmp = abs(sum_data - (sum_data - data[i]))
  min_abs = min(min_abs, tmp)
  if min_abs == tmp:
    min_i = i

print(sum_data - data[min_i])