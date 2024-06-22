MOD = 998244353

N, K = map(int, input().split())
S = input()

def is_palindrome(s):
	return s == s[::-1]

# dp[pos][mask] : pos 位置まで見て、直近K文字がmaskである場合の数
dp = [[0] * (1 << K) for _ in range(N+1)]
dp[0][0] = 1  # 初期状態

for i in range(N):
	for mask in range(1 << K):
		current_chars = ['A', 'B']
		if S[i] != '?':
			current_chars = [S[i]]

		for char in current_chars:
			next_mask = ((mask << 1) & ((1 << K) - 1)) | (1 if char == 'A' else 0)
			if i + 1 >= K:
				# 直近K文字をチェックして回文でないか確認
				if not is_palindrome(bin(next_mask)[2:].zfill(K).replace('0', 'B').replace('1', 'A')):
					dp[i+1][next_mask] = (dp[i+1][next_mask] + dp[i][mask]) % MOD
			else:
				dp[i+1][next_mask] = (dp[i+1][next_mask] + dp[i][mask]) % MOD

print(sum(dp[N][mask] for mask in range(1 << K)) % MOD)