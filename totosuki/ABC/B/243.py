import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt1 = int()
cnt2 = int()

for a, b in zip(A, B):
  if a == b:
    cnt1 += 1
  elif a in B:
    cnt2 += 1

print(cnt1, cnt2, sep = "\n")