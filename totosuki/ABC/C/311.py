import sys
input = sys.stdin.buffer.readline

N = int(input())
A = list(map(int, input().split()))
n_i = 1
memo_se = {1}
memo_li = [1]

i = 0
while i < N:
  n_i = A[n_i-1]

  if n_i in memo_se:
    id = memo_li.index(n_i)
    print(len(memo_li[id:]))
    print(*memo_li[id:])
    break
  
  memo_se.add(n_i)
  memo_li.append(n_i)

  i += 1


