import sys
input = sys.stdin.buffer.readline

N = bin(int(input()))[2:]
L = []

for i in range(len(N)):
  if N[-i-1] == "1":
    L.append(i)

for i in range(2**len(L)):
  use = []
  rslt = 0
  
  for j in range(len(L)):
    if (i >> j) & 1:
      use.append(L[j])
  
  for n in use:
    rslt += 2 ** n
  
  print(rslt)