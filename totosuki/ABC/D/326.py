from itertools import permutations

N = int(input())
R = list(input()) # 右に必ずくる文字
C = list(input()) # 上に必ず来る文字

R_permutation_list = [] # 置ける可能性のある文字の組み合わせ
C_permutation_list = [] # 置ける可能性のある文字の組み合わせ

for r in R:
  tmp = []
  for i in range(N - 2):
    if r == "A":
      tmp.append(permutations("BC"+"."*i))
    elif r == "B":
      tmp.append(permutations("AC"+"."*i))
    else:
      tmp.append(permutations("AB"+"."*i))
  R_permutation_list.append(tmp)

for c in C:
  tmp = []
  for i in range(N - 2):
    if c == "A":
      tmp.append(permutations("BC"+"."*i))
    elif c == "B":
      tmp.append(permutations("AC"+"."*i))
    else:
      tmp.append(permutations("AB"+"."*i))
  C_permutation_list.append(tmp)

for R_perm in R_permutation_list:
  for C_perm in C_permutation_list:
    for r_perm in R_perm:
      for c_perm in C_perm:
        print(r_perm, c_perm)

