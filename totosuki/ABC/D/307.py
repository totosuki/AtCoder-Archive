import sys, collections
input = sys.stdin.buffer.readline

N = int(input())
S = input().decode().strip()
l_cnt = 0

queue = collections.deque()

for i in range(N):
  if S[i] == "(":
    l_cnt += 1
    queue.append(S[i])
  elif S[i] == ")":
    if l_cnt > 0:
      while True:
        if queue.pop() == "(":
          l_cnt -= 1
          break
    else:
      queue.append(S[i])
  else:
    queue.append(S[i])

print("".join(queue))