from collections import deque

T = int(input())

def flat(S: str):
    q = deque([])
    for s in S:
        q.append(s)
        if len(q) >= 4 and q[-4]+q[-3]+q[-2]+q[-1] == "(xx)":
                for _ in range(4): q.pop()
                q.append("x"); q.append("x")
    return q

for _ in range(T):
    A = input()
    B = input()
    print("Yes" if flat(A) == flat(B) else "No")






# AとB両方をできるだけ限界まで外してみる

# stbも同じ
# 左括弧, x, 右括弧の数, sta追加後の文字列の保持をする。
# 左括弧開始時にstの値を全てstaに入れる
# xが3つを超えたタイミングでそれまでの左括弧, xをstaに入れる
# 右括弧が生まれたら左括弧の数を一つ減らす。