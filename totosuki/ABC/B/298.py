def rotate_array(A):
  new_A = []
  for i in range(N):
    flatten_A = list(itertools.chain.from_iterable(A[::-1]))
    tmp = []
    for j in range(i, N*N, N):
      tmp.append(flatten_A[j])
    new_A.append(tmp)
  return new_A

import itertools

N = int(input())
A = []
B = []
for _ in range(N):
  A.append(list(map(int, input().split())))
for _ in range(N):
  B.append(list(map(int, input().split())))

for _ in range(4):
  flag = True
  A_1 = []
  flatten_A = list(itertools.chain.from_iterable(A))
  flatten_B = list(itertools.chain.from_iterable(B))

  for a, b in zip(flatten_A, flatten_B):
    if a == 1 and b == 0:
      flag = False

  if flag:
    print("Yes")
    exit()

  A = rotate_array(A)

print("No")