n = int(input())
a = list(map(int,input().split()))
answer = 0
for i in a:
    cnt = 0
    while True:
        if (i - cnt)%2 == 1 and not (i - cnt)%3 == 2:
            answer = answer + cnt
            break
        else:
            cnt = cnt + 1
print(answer)