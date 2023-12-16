S1,S2 = input()
T1,T2 = input()
# 正五角形
alpha = ["A","B","C","D","E"]

s1_id = alpha.index(S1)
S_len = 0

if s1_id+1 == 5:
  id_plus = 0
else:
  id_plus = s1_id+1

if alpha[s1_id-1] == S2 or alpha[id_plus] == S2:
  S_len = 1
else:
  S_len = 2

t1_id = alpha.index(T1)
T_len = 0

if t1_id+1 == 5:
  id_plus = 0
else:
  id_plus = t1_id+1

if alpha[t1_id-1] == T2 or alpha[id_plus] == T2:
  T_len = 1
else:
  T_len = 2

print("Yes" if S_len == T_len else "No")