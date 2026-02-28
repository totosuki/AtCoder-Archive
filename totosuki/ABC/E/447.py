from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n
    
    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        
        if x == y:
            return
        
        if self.parents[x] > self.parents[y]:
            x, y = y, x
        
        self.parents[x] += self.parents[y]
        self.parents[y] = x
    
    def size(self, x):
        return -self.parents[self.find(x)]
            
    def same(self, x, y):
        return self.find(x) == self.find(y)
    
    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]
    
    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]
    
    def group_count(self):
        return len(self.roots())
    
    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members
    
    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())


from collections import defaultdict

N, M = map(int, input().split())
U = [0] * M
V = [0] * M
cost = [0] * M
mod = 998244353

for i in range(M):
    u, v = map(int, input().split())
    U[i] = u-1
    V[i] = v-1


    cost[i] = cost[i-1] * 2 if i else 2
    cost[i] %= mod

uf = UnionFind(N)
ans = 0
cnt = N

for i in range(M-1, -1, -1):
    if not uf.same(U[i], V[i]):
        if cnt > 2:
            uf.union(U[i], V[i])
            cnt -= 1
        else:
            ans += cost[i]
            ans %= mod

print(ans)
