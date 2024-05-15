S = list(input())
T = list(input())

j = 0
ans = []
for i in range(len(T)):
    if T[i] == S[j]:
        j += 1
        ans.append(i+1)

print(*ans)

