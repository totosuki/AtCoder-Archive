import sys
input = sys.stdin.buffer.readline

def enum_divisors(N: int) -> list:
  x = 1
  rslt = []
  while x * x <= N:
    if N % x == 0:
      rslt.append(x)
      # 重複しないならば i の相方の N/i も append
      if N/x != x:
        rslt.append(N//x)
    x += 1
  rslt.sort()
  return rslt

N = int(input())
rslt = enum_divisors(N)

print(*rslt)