N, T = input().split()
N = int(N)
len_T = len(T)
rslt = []

for i in range(1, N+1):
  S = input()
  # print(S, "===")
  
  flag = False
  
  if T == S: # TとSが同じ文字列の場合
    flag = True
  elif len_T == (len(S) - 1): # Tのいずれかの位置に1文字挿入した場合
    cnt = 0
    j = 0
    while j < len_T:
      if cnt > 1:
        break
      if T[j] != S[j+cnt]:
        cnt += 1
      else:
        j += 1
    if cnt == 1 or cnt == 0:
      flag = True
  elif len_T == (len(S) + 1): # Tのいずれかの位置の1文字を削除した場合
    cnt = 0
    j = 0
    while j < len(S):
      if cnt > 1:
        break
      if T[j+cnt] != S[j]:
        cnt += 1
      else:
        j += 1
    if T[len_T-1] != S[len(S)-1] and cnt == 0:
      flag = True
    if cnt == 1:
      flag = True
  elif len_T == len(S): # Tのいずれかの位置の1文字を置換した場合
    cnt = 0
    for j in range(len_T):
      if T[j] != S[j]:
        cnt += 1
    if cnt == 1:
      flag = True
  
  if flag:
    rslt.append(i)

print(len(rslt))
print(*rslt)