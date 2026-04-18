N, M = map(int, input().split())
F = list(map(int, input().split()))

ans1 = False
ans2 = True

if len(set(F)) == len(F):
    ans1 = True

for m in range(1, M+1):
    if m not in F:
        ans2 = False

print("Yes" if ans1 else "No")
print("Yes" if ans2 else "No")
