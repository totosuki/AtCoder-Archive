import os, io, string, collections

_f, _nl = io.BytesIO(), int()
def input():
  global _nl
  p = _f.tell()
  while not _nl:
    mb = os.fstat(0)
    bd = os.read(0, mb.st_size)
    _nl = bd.count(b'\n') + (not bd)
    _f.seek(0, 2)
    _f.write(bd)
  _f.seek(p)
  _nl -= 1
  return _f.readline()

alpha = string.ascii_lowercase
N, K = map(int, input().split())
S = [input().decode().strip() for _ in range(N)]
rslt = []

for i in range(2**N):
  check = []
  alpha_cnt = collections.Counter()
  
  for j in range(N):
    if (i >> j) & 1:
      check.append(S[j])
  
  for s in check:
    for j in range(26):
      if alpha[j] in s:
        alpha_cnt[j] += 1
  
  sm = sum(1 for cnt in alpha_cnt.values() if cnt == K)
  rslt.append(sm)

print(max(rslt))