import sys
input = sys.stdin.buffer.readline

N = int(input())
A = map(int, input().split())
B = map(int, input().split())
rslt = int()

for a,b in zip(A, B):
  rslt += a*b

print("Yes") if rslt == 0 else print("No")