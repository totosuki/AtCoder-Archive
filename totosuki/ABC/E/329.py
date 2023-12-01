from collections import deque

def check(M,S,T,i):
  flag = True
  for j in range(M):
    flag = flag and (S[i+j] == T[j] or S[i+j] == "#")
  return flag

def return_deque(N,M,S,T):
  ok = [True] * N
  q = deque()
  for i in range(N-M+1):
    if check(M,S,T,i):
      ok[i] = False
      q.append(i)
  return q, ok

def solve(N,M,S,T,q:deque,ok):
  while q:
    now = q.pop()
    S[now:now+M] = ["#"] * M
    for i in range(now-M+1, now+M):
      if 0 <= i < N-M+1 and ok[i]:
        if check(M,S,T,i):
          ok[i] = False
          q.append(i)
  return set(S)

def main():
  N, M = map(int, input().split())
  S = list(input())
  T = list(input())
  q, ok = return_deque(N,M,S,T)
  rslt = solve(N,M,S,T,q,ok)
  
  print("Yes" if len(rslt) == 1 and list(rslt)[0] == "#" else "No")

main()
