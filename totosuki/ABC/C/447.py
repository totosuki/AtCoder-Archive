S = input()
T = input()

si = len(S)-1
ti = len(T)-1
cnt = 0

while True:
    if ti == -1 and si == -1:
        break
    elif ti == -1:
        if S[si] != "A":
            cnt = -1
            break
        else:
            si -= 1
            cnt += 1
            continue
    elif si == -1:
        if T[ti] != "A":
            cnt = -1
            break
        else:
            ti -= 1
            cnt += 1
            continue

    if S[si] != T[ti]:
        if T[ti] == "A":
            ti -= 1
            cnt += 1
        elif S[si] == "A":
            si -= 1
            cnt += 1
        else:
            cnt = -1
            break
    else:
        ti -= 1
        si -= 1

print(cnt)
