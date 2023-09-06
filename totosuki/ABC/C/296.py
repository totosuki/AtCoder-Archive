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

N, X = map(int, input().split())
A = list(map(int, input().split()))
j = 0
A.sort(reverse = True)
answer = "No"

for i in range(N):
  while (A[i] - A[j] <= X) and (j < N-1):
    if A[i] - A[j] == X:
      answer = "Yes"
    j += 1

print(answer)