S = input()

acc = [0] * (len(S)+1)
acc[0] += S[0] == "A"

acc_c = [0] * (len(S)+1)

cnt = 0

for i in range(1, len(S)):
    # print(f"i: {i}, acc: {acc}")

    acc[i] += acc[i-1]
    acc_c[i] += acc_c[i-1]

    acc[i] = max(0, acc[i])
    acc_c[i] = max(0, acc_c[i])

    if S[i] == "A":
        acc[i] += 1
    elif S[i] == "B":
        acc[i+1] -= 1
        acc_c[i] += acc[i] >= 1
    else:
        acc_c[i+1] -= 1
        cnt += acc_c[i] >= 1

print(cnt)
