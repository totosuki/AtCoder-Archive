import sys
readline = sys.stdin.buffer.readline

def f(n):
  rslt = 0
  for _ in range(n):
    A, B = map(int, readline().split())
    rslt += ((B*(B+1))//2) - ((A-1)*A//2)
  return rslt

N = int(readline())
print(f(N))