N = int(input())
ans = 0

for _ in range(N):
    A, B, S = input().split()
    A = int(A)
    B = int(B)
    if S == "keep":
        ans += B - A

print(ans)
