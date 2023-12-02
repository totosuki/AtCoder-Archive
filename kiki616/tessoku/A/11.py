N,X = map(int,input().split())
A = [0] + list(map(int,input().split()))
mn = 1
mx = N
index = mn+((mx - mn)//2)

while True:
  if A[index] == X:
    print(index)
    break
  else:
    if A[index] < X:
      mn = index+1
      index = mn+((mx - mn)//2)
    elif A[index] > X:
      mx = index-1
      index = mn+((mx - mn)//2)