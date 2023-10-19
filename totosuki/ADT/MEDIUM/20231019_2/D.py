from collections import defaultdict

N, M, T = map(int, input().split())
A = [0] + list(map(int, input().split())) # 次の部屋に行くためのコストとして捉える
dict = defaultdict(int)
answer = "Yes"

for _ in range(M):
  x, y = map(int, input().split())
  dict[x] = y



for i in range(1, N):
  if dict[i] != 0:
    T += dict[i]
  T -= A[i]
  if T <= 0:
    answer = "No"

print(answer)