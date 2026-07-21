N = int(input())
S = input()

ans = [0] * N
rev = False
l = 0
r = N-1

for i in range(N, 0, -1):
    if S[i-1] == "o":
        rev = not rev

    if rev:
        ans[l] = i
        l += 1
    else:
        ans[r] = i
        r -= 1
    
    if r - l < 0:
        break

print(*ans)
