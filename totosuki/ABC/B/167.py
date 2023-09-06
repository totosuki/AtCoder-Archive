import sys
read = sys.stdin.buffer.read

A, B, C, K = map(int, read().split())
rslt = 0

if K >= A:
  rslt += A
  K -= A
else:
  rslt += K
  K = 0

if K >= B:
  K -= B
else:
  K = 0

rslt -= K

print(rslt)