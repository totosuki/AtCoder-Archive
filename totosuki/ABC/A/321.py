N = list(input())
N_sort = sorted(N, reverse=True)
N_set = set(N)
print("Yes") if N == N_sort and len(N) == len(N_set) else print("No")