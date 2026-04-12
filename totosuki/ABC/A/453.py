N = int(input())
S = input()

ans = ""
id = len(S)

for i in range(len(S)):
    if S[i] == "o":
        continue
    else:
        id = i
        break

print(S[id:])