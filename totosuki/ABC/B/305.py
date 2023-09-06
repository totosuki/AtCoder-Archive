length = [3, 1, 4, 1, 5, 9]
abc = "ABCDEFG"
P, Q = input().split()
P_i = abc.index(P)
Q_i = abc.index(Q)
if P_i < Q_i:
  rslt = length[P_i:Q_i]
  print(sum(rslt))
else:
  rslt = length[Q_i:P_i]
  print(sum(rslt))