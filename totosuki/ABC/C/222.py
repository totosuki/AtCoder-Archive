import os, io
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

N, M = map(int, input().split())
data = [input().decode().strip() for _ in range(2*N)]
rank = [[0, i+1] for i in range(2*N)]

for i in range(M):
  for j in range(1, N+1):
    j *= 2
    a = rank[j-1-1][1]
    b = rank[j-1][1]
    a_h = data[a-1][i]
    b_h = data[b-1][i]
    tmp = a_h + b_h
    if tmp in {"GC", "CP", "PG"}:
      rank[j-1-1][0] -= 1
    elif tmp in {"CG", "PC", "GP"}:
      rank[j-1][0] -= 1
    else:
      continue
  
  rank.sort()

[print(r[1]) for r in rank]