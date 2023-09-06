N,K = map(int,input().split())
answer = K
friend = []
for i in range(N):
    A,B = map(int,input().split())
    friend.append([A,B])

friend.sort()

for i in friend:
    A,B = i[0],i[1]
    if answer >= A:
        answer = answer + B
    else:
        break
print(answer)