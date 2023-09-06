N, A, B = map(int, input().split())
result = []

for n in range(1, N+1):
  n_list = [int(n) for n in str(n)]
  n_sum = sum(n_list)
  if A <= n_sum and n_sum <= B:
    result.append(n)

print(sum(result))