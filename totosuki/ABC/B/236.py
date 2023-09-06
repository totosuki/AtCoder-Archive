import sys, collections
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
cnt = dict(collections.Counter(A))

for k, i in cnt.items():
  if i == 3:
    print(k)