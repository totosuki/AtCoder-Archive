def return_C(S, T, K):
  C = [K] * 10
  for s in S: C[s] -= 1
  for t in T: C[t] -= 1
  return C

def score(L):
  score = 0
  cnt = [0] * 10
  for num in L: cnt[num] += 1
  for i in range(1, 10): score += i*(10**cnt[i])
  return score

def main():
  K = int(input())
  S = list(map(int, input()[:4]))
  T = list(map(int, input()[:4]))
  C = return_C(S, T, K)
  all_cnt = (9*K-8) * (9*K-9)
  win_cnt = 0
  for i in range(1, 10): # S
    for j in range(1, 10): # T
      if C[i] == 0 or C[j] == 0: continue
      if i == j and C[i] <= 1: continue
      SI = S + [i]
      TJ = T + [j]
      if score(SI) > score(TJ):
        if i == j:
          win_cnt += C[i] * (C[i]-1)
        else:
          win_cnt += C[i] * C[j]
  print(win_cnt / all_cnt)

main()