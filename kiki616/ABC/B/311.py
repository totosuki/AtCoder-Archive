N,D = map(int,input().split())
schedule = []
cnt = 0
answer = []
for i in range(N):
    schedule.append(input())

for i in range(D):
    isis = True
    for l in range(N):
        if schedule[l][i] != "o":
            isis = False
    if isis:
        cnt += 1
    else:
        answer.append(cnt)
        cnt = 0
if answer:
    print(max(answer))
else:
    print(D)

# N,D = map(int,input().split())
# schedule = []
# holiday = ["o" for i in range(D)]
# for i in range(N):
#     schedule.append(input())

# for i in range(N):
#     holi = []
#     for l in range(D):
#         if holiday[l] == "o" and schedule[i][l] == "o":
#             holi.append("o")
#         else:
#             holi.append("x")
#     holiday = holi
    
# print(holiday.count("o"))