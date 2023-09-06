# import numpy as np
N = int(input())
X = list(map(int, input().split()))
X.sort()
print(sum(X[N:-N]) / (N*3))
# X = np.array(list(map(int, input().split())))
# X = np.sort(X)
# print(np.mean(np.sort(X)[N:-N]))