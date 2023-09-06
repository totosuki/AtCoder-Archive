import sys, collections
input = sys.stdin.buffer.readline

N = int(input())
S = [input().decode().strip() for _ in range(N)]
mx_S = str()
cnt = dict(collections.Counter(S))

for k, i in cnt.items():
  if i == max(cnt.values()):
    mx_S = k

print(mx_S)