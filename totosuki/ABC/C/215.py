import sys, itertools
input = sys.stdin.buffer.readline

S, K = input().decode().strip().split()
K = int(K)
perm = sorted(list(set(itertools.permutations(S, len(S)))))
perm = ["".join(p) for p in perm]

print("".join(perm[K-1]))