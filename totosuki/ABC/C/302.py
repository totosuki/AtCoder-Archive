from itertools import permutations

def solve(N, M, S):
  answer = "No"
  for ps in permutations(S):
    ok = True
    for i in range(N-1):
      s = ps[i]
      ns = ps[i+1]
      diff = 0
      for j in range(M):
        if s[j] != ns[j]:
          diff += 1
      ok = (diff == 1)
      if not ok:
        break
    if ok:
      answer = "Yes"
  print(answer)

def main():
  N, M = map(int, input().split())
  S = [list(input()) for _ in range(N)]
  solve(N, M, S)

main()