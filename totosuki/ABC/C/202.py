import sys, collections
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
rslt = 0

A_dict = collections.defaultdict(int)
for a in A:
  A_dict[a] += 1

for c in C:
  b = B[c-1]
  if b in A_dict:
    A_cnt = A_dict[b]
    rslt += A_cnt

print(rslt)