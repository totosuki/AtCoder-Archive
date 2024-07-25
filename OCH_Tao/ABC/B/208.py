P = int(input())
X = [3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1]
cnt = 0
for i in X:
  cnt+=P//i
  P%=i
print(cnt)