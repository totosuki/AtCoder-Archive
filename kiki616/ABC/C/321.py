K = int(input())
li = []
ans = 0
cnt = 1
a = [0,1,2,3,4,5,6,7,8,9]
for h in range(10):
    li.append(int(str(h)))
    for j in range(h):
        li.append(int(str(h)+str(j)))
        for i in range(j):
            li.append(int(str(h)+str(j)+str(i)))
            for l in range(i):
                li.append(int(str(h)+str(j)+str(i)+str(l)))
                for f in range(l):
                    li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)))
                    for d in range(f):
                        li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)+str(d)))
                        for s in range(d):
                            li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)+str(d)+str(s)))
                            for a in range(s):
                                li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)+str(d)+str(s)+str(a)))
                                for q in range(a):
                                    li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)+str(d)+str(s)+str(a)+str(q)))
                                    for w in range(q):
                                        li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)+str(d)+str(s)+str(a)+str(q)+str(w)))
                                        for e in range(w):
                                            li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)+str(d)+str(s)+str(a)+str(q)+str(w)+str(e)))
                                            for r in range(e):
                                                li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)+str(d)+str(s)+str(a)+str(q)+str(w)+str(e)+str(r)))
                                                for t in range(r):
                                                    li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)+str(d)+str(s)+str(a)+str(q)+str(w)+str(e)+str(r)))
                                                    for y in range(t):
                                                        li.append(int(str(h)+str(j)+str(i)+str(l)+str(f)+str(d)+str(s)+str(a)+str(q)+str(w)+str(e)+str(r)+str(y)))
li.sort()
print(li[K])
# for i in range(1,K+1):
#     if 
#     ans = i * cnt
# print(ans)

# memo
# 1,2,3,4,5,6,7,8,9,
# 10,21,20,32,31,30,43,42,41,40,
# 11