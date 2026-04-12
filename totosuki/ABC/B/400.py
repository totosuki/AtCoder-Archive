N, M = map(int, input().split())
ans = 0

for i in range(M+1):
    ans += N**i
    if ans > 10**9:
        break
else:
    print(ans)
    exit()

print("inf")
