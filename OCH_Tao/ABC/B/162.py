N = int(input())
print(sum([i for i in list(range(1,N+1)) if i%3!=0 and i%5!=0]))