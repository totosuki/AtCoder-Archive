# H, W = map(int, input().split())

# ans = ["." * W] * H


# ans[0] = "#" * W
# ans[-1] = "#" * W

# for i in range(1, H-1):
#     text = "#" + "." * (W-2) + "#"
#     ans[i] = text

# for i in range(H):
#     print(*ans[i], sep="")


# 82byte
# h,w=map(int,input().split());[print('#'+'#.'[0<i<h-1]*(w-2)+'#')for i in range(h)]

# 81byte
# h,w=map(int,input().split())
# for i in range(h):print('#'+'#.'[0<i<h-1]*(w-2)+'#')

# 80byte
# h,w=map(int,input().split())
# for i in range(h):print(f"#{'#.'[0<i<h-1]*(w-2)}#")

# 77byte
h,w=map(int,input().split());print('#'*w+'\n'+f"#{'.'*(w-2)}#\n"*(h-2)+'#'*w)

