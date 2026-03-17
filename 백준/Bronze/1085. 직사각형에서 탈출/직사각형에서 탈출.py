x, y, w, h = map(int, input().split())

len1 = y
len2 = h - y
len3 = x
len4 = w - x

print(min(len1, len2, len3, len4))