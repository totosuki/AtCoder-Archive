import os, io; from collections import defaultdict
_f, _nl, _mb = io.BytesIO(), int(), 10**6
def input():
  global _nl
  p = _f.tell()
  while not _nl:
    bd = os.read(0, _mb)
    _nl = bd.count(b'\n') + (not bd)
    _f.seek(0, 2)
    _f.write(bd)
  _f.seek(p)
  _nl -= 1
  return _f.readline()

N = int(input())
dict = defaultdict(int)
score = list()

for i in range(1, N+1):
  S, T = input().decode().rstrip().split()
  T = int(T)

  if dict[S] == 0:
    score.append([-T, i])

  dict[S] += 1

score.sort()

print(score[0][1])