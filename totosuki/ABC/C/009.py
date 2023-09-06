import sys
input = sys.stdin.buffer.readline

N, K = map(int, input().split())
s = input().decode().strip()

rslt = list(s)

for i in range(N):
  l = i
  
  for j in range(i+1, N):
    # 現在の i 番目の文字より小さい文字があるか探す
    if rslt[l] > rslt[j]:
      # あったら
      ss = rslt.copy()
      ss[i], ss[j] = ss[j], ss[i]

      # ss と s を比較
      diff = 0
      for t in range(N):
        if ss[t] != s[t]:
          diff += 1
      if diff <= K:
        l = j
  
  rslt[i], rslt[l] = rslt[l], rslt[i]

print("".join(rslt))

# SampleはAC 2
# N, K = map(int, input().split())
# S = list(input().decode().strip())
# T = copy.deepcopy(S)
# S_sorted = sorted(list(S))

# for i in range(N):
  
#   t = T[i]

#   if S[i] != S_sorted[i]:
#     change_i = T.index(S_sorted[i])
  
#     next_T = copy.deepcopy(T)
#     next_T[i] = S_sorted[i]
#     next_T[change_i] = t

#     cnt = 0
#     for t, s in zip(next_T, S):
#       if t != s:
#         cnt += 1
    
#     if cnt <= K:
#       T = copy.deepcopy(next_T)

# print("".join(T))

# SampleはAC
# N, K = map(int, input().split())
# S = list(input().decode().strip())
# T = copy.deepcopy(S)
# S_sorted = sorted(list(S))

# for i in range(N):
#   t = T[i]
#   if S[i] != S_sorted[i] and K > 1:
#     change_i = T.index(S_sorted[i])
#     T[i] = S_sorted[i]
#     T[change_i] = t
#     K -= 1

# print("".join(T))