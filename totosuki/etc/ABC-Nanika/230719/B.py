import sys, collections
input = sys.stdin.buffer.readline

N, M, T = map(int, input().split())
A = list(map(int, input().split()))
X = set()
Y = collections.deque()
for _ in range(M):
  x, y = map(int, input().split())
  X.add(x)
  Y.append(y)

answer = "Yes"

for i in range(N-1):
  T -= A[i]

  if i+1 in X:
    T += Y.popleft()
  
  if T <= 0:
    answer = "No"

print(answer)
