N = int(input())
W = input().strip(".").split()
cnt = 0
cnt+=W.count("TAKAHASHIKUN")
cnt+=W.count("Takahashikun")
cnt+=W.count("takahashikun")
print(cnt)