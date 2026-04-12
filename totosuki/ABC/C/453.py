N = int(input())
L = list(map(int, input().split()))
ans = 0

for bit in range(1<<N):
    now = next = 0.5
    cnt = 0

    for i in range(N):
        if bit & (1 << i):
            next = now + L[i]
        else:
            next = now - L[i]
        
        if (next > 0) != (now > 0):
            cnt += 1

        now = next
    
    ans = max(ans, cnt)

print(ans)

# bit が立っている時にプラスに進ませる
