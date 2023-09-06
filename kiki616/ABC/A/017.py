# print([i[0] for i in [list(map(int, input().split())) for _ in range(3)]])
# sum(map(lambda s,e: s * e*0.1, i[0],i[1] ))

answer = int()
for i in range(3):
    s,e = map(int, input().split())
    answer = answer + s * (e/10)

print(int(answer))
