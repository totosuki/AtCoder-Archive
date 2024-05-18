import math

def get_base_A(A):
  if A % 4 == 0  :return A
  elif A % 4 == 1:return A + 3
  elif A % 4 == 2:return A + 2
  else           :return A + 1

def get_base_C(C):
  if C % 4 == 0  :return C
  elif C % 4 == 1:return C - 1
  elif C % 4 == 2:return C - 2
  else           :return C - 3

def kakutei(A, B, C, D):
  base_A = get_base_A(A)
  base_C = get_base_C(C)
  dist_bd = D - B
  
  if base_A >= base_C:
    return 0
  else:
    return ((base_C - base_A) * dist_bd) / 2

def left_3(A, B, C, D):
  if B % 2 == 0:
    return math.ceil((D - B) / 2) / 2
  else:
    return math.floor((D - B) / 2) / 2

def left_2(A, B, C, D):
  if B % 2 == 0:
    return math.floor((D - B) / 2) / 2
  else:
    return math.ceil((D - B) / 2) / 2

def left_1(A, B, C, D):
  white = 0
  if B % 2 == 0:
    white = math.ceil((D - B) / 2)
  else:
    white = math.floor((D - B) / 2)
  white /= 2
  return ((D - B) - white)

def left(A, B, C, D):
  if A % 4 == 0:return 0
  
  if A % 4 == 3:
    return left_3(A, B, C, D)
  
  if A % 4 == 2:
    if C - A == 1:
      return left_2(A, B, C, D)
    else:
      return left_2(A, B, C, D) + left_3(A, B, C, D)
  
  if A % 4 == 1:
    if C - A == 1:
      return left_1(A, B, C, D)
    elif C - A == 2:
      return left_1(A, B, C, D) + left_2(A, B, C, D)
    else:
      return left_1(A, B, C, D) + left_2(A, B, C, D) + left_3(A, B, C, D)

def right_1(A, B, C, D):
  white = 0
  if B % 2 == 0:
    white = math.floor((D - B) / 2)
  else:
    white = math.ceil((D - B) / 2)
  white /= 2
  return ((D - B) - white)

def right(A, B, C, D):
  if C % 4 == 0:return 0
  
  if C % 4 == 1:
    return right_1(A, B, C, D)
  
  if C % 4 == 2:
    if C - A == 1:
      return 0 # すでにleftで計算済み
    else:
      return right_1(A, B, C, D) + left_1(A, B, C, D)
  
  if C % 4 == 3:
    if C - A <= 2:
      return 0 # すでにleftで計算済み
    else:
      return right_1(A, B, C, D) + left_1(A, B, C, D) + left_2(A, B, C, D)

def main():
  A, B, C, D = map(int, input().split())
  ans = 0
  ans += kakutei(A, B, C, D)
  ans += left(A, B, C, D)
  ans += right(A, B, C, D)
  print(int(round(ans * 2)))

main()

# (0,0)を基準に横に4,縦に1広がると2だけの黒面積ができる

# 定位置（0,0）からの確定面積をまず求める