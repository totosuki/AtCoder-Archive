from numpy import roll
N = int(input())
A = []
for i in range(N):
  A.append(list(input()))
ans = []
for i in A:
  ans.extend([int("".join(roll(i,j))) for j in range(N)])
  ans.extend([int("".join(reversed(roll(i,j)))) for j in range(N)])
for i in range(N):
  X = [j[i] for j in A]
  ans.extend([int("".join(roll(X,j))) for j in range(N)])
  ans.extend([int("".join(reversed(roll(X,j)))) for j in range(N)])
for i in range(N):
  X = [j%N for j in range(i,i+N)]
  Y = [j%N for j in range(i,i-N,-1)]
  X2 = [A[j][X[j]] for j in range(N)]
  Y2 = [A[j][Y[j]] for j in range(N)]
  ans.extend([int("".join(roll(X2,j))) for j in range(N)])
  ans.extend([int("".join(reversed(roll(X2,j)))) for j in range(N)])
  ans.extend([int("".join(roll(Y2,j))) for j in range(N)])
  ans.extend([int("".join(reversed(roll(Y2,j)))) for j in range(N)])
print(max(ans))