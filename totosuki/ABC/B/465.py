X, Y, L, R, A, B = map(int, input().split())
ans = 0

for i in range(1, 24):
    if A < i <= B:
        if L < i <= R:
            ans += X
        else:
            ans += Y

print(ans)