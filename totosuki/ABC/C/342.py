N = int(input())
S = input()
Q = int(input())

char_map = {chr(i): chr(i) for i in range(97, 123)} 

for _ in range(Q):
  c, d = input().split()
  # すべてのキーに対して、cをdに置き換える
  for key in char_map:
    if char_map[key] == c:
      char_map[key] = d

# 置き換えられた文字列を生成
result = ''.join([char_map[char] for char in S])

print(result)
# 考察
# 辞書のデータ構造で行けそう