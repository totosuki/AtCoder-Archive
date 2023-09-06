import sys
input = sys.stdin.buffer.readline

N = int(input())
A = map(int, input().split())
B = map(int, input().split())
cnt = 0
min_n = 0
max_n = 1005

for a, b in zip(A, B):
  if min_n < a:
    min_n = a
  if max_n > b:
    max_n = b

if min_n > max_n:
  print(0)
else:
  print(max_n - min_n + 1)