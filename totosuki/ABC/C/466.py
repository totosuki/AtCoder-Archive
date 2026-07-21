N = int(input())
cnt = 0
bak = 2
for l in range(1, N):
    for r in range(max(l+1, bak), N+1):
        print("?", l, r, flush=True)
        ans = input()
        if ans == "No":
            bak = r
            cnt += r - l - 1
            break
    else:
        bak = N
        cnt += r - l

print("!", cnt, flush=True)
