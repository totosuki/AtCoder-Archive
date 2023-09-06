N = int(input())
H = list(map(int,input().split()))
number = 0
for i in range(1,N):
  if H[i -1] < H[i]:
    number += 1
  else:
    break
print(H[number])