N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

mx_A = max(A)
mn_B = min(B)

print(0) if mx_A > mn_B else print(mn_B - mx_A + 1)