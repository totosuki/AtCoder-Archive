import copy
from itertools import permutations

def return_maisuu(L):
  maisuu = [0] * 10
  for i in range(4):
    card = int(L[i])
    maisuu[card] += 1
  return maisuu

def return_pettern(L, K, maisuu):
  pettern = [list(map(int, copy.copy(L[:4]))) for _ in range(9)]
  pettern = []
  for num in range(1, 10):
    pettern.append(list(map(int, copy.copy(L[:4]))) + [num])
  return pettern

def return_score(L):
  cnt = [0] * 10
  for num in L:
    cnt[num] += 1
  score = 0
  for i in range(10):
    score += i * 10**cnt[i]
  return score

def can_battle(S, T, K):
  cnt = [0] * 10
  can = True
  for s in S:
    cnt[s] += 1
  for t in T:
    cnt[t] += 1
  for c in cnt:
    if c > K:
      can = False
  return can

def check(S_pettern, T_pettern, K):
  all_cnt = 0
  win_cnt = 0
  for S in S_pettern:
    for T in T_pettern:
      if can_battle(S, T, K):
        all_cnt += 1
        S_score = return_score(S)
        T_score = return_score(T)
        
        print(f"S : {S}, T : {T}, S_score : {S_score}, T_score : {T_score}")
        
        if S_score > T_score:
          win_cnt += 1
  return win_cnt, all_cnt


def main():
  K = int(input())
  S = list(input())
  T = list(input())
  maisuu_S = return_maisuu(S)
  maisuu_T = return_maisuu(T)
  S_pettern = return_pettern(S, K, maisuu_S)
  T_pettern = return_pettern(T, K, maisuu_T)
  win_cnt, all_cnt = check(S_pettern, T_pettern, K)
  print(win_cnt, all_cnt)
  print(win_cnt / all_cnt)

main()