N = int(input())
S = input()
X = []

for i in range(N):
    if S[i] == "x": X.append(i+1)

for x in X: print(x)

print(f"{N}\n" * (N - len(X)), end="")
