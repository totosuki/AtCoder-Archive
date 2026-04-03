import heapq

Q = int(input())
tree = []
heapq.heapify(tree)

for _ in range(Q):
    t, h = map(int, input().split())

    if t == 1:
        heapq.heappush(tree, h)
    else:
        while len(tree):
            x = heapq.heappop(tree)
            if x > h:
                heapq.heappush(tree, x)
                break
    
    print(len(tree))
