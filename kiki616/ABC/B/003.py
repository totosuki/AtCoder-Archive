S = input()
T = input()
atcoder = ["a","t","c","o","d","e","r","@"]
answer = True
for i in range(len(S)):
    if (S[i] == T[i]) or (S[i] == "@" and T[i] in atcoder) or (T[i] == "@" and S[i] in atcoder):
        pass
    else:
        answer = False

if answer:
    print("You can win")
else:
    print("You will lose")