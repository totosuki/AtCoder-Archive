n,a,b = map(int,input().split())

# 地道君
# answer = [ i for i in range(n+1) ]
# for i in answer:

# 11絶対教のやり方(range(n+1)はif文書いて処理量を減らす方が本当はいい)
answer = [i for i in range(n+1) if a <= i and b >= i]

print(answer)