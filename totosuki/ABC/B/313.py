import os, io
_f, _nl, _mb = io.BytesIO(), int(), 10**5
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

N, M = map(int, input().split())
A = []
B = []
saikyo = [True] * N

exec("a,b=map(int,input().split());A.append(a);B.append(b);"*M)

for b in B:
  saikyo[b-1] = False

if sum(saikyo) == 1:
  print(saikyo.index(True) + 1)
else:
  print(-1)