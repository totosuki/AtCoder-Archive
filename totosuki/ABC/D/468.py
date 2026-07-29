S = input()
N = len(S)
cnt = 0

# odd
for i in range(N):
    cnt += 1
    dst = 1
    flag = False
    while i-dst >= 0 and i+dst < N:
        if S[i-dst] != S[i+dst]:
            if flag: break
            else: flag = True
        cnt += 1
        dst += 1

# even
for i in range(N-1):
    dst = 0
    flag = False
    while i-dst >= 0 and i+dst+1 < N:
        if S[i-dst] != S[i+dst+1]:
            if flag: break
            else: flag = True
        cnt += 1
        dst += 1

print(cnt)
