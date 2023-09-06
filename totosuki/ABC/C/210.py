import sys, collections
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
C = list(map(int, input().split()))
dict = collections.defaultdict(int)
len_dict = 0
now = 0
mx = 0

for i in range(N):
  if len_dict >= K:
    dict[C[i-K]] -= 1
    if dict[C[i-K]] == 0:
      now -= 1
  
  if dict[C[i]] == 0:
    now += 1
  dict[C[i]] += 1
  len_dict += 1

  mx = max(mx, now)

print(mx)