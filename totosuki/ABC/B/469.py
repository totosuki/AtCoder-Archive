N = int(input())
S = "x" + input() + "x"
cnt = 0

for i in range(1, N+1):
    flag = 0
    flag += S[i] == "x"
    flag += S[i-1] == "x"
    flag += S[i+1] == "x"
    cnt += flag == 3

print(cnt)
