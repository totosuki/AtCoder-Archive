P, Q, R = map(int, input().split())

answer = 5000

answer = min(5000, P+Q, Q+R, R+P)

print(answer)