import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
koma = list()
P = 0

for a in A:
  koma.append(0)
  for i in range(len(koma)):
    koma[i] += a

for k in koma:
  if k >= 4:
    P += 1

print(P)