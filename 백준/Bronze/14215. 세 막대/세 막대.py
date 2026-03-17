# 정수 입력받기
a,b,c, = map(int, input().split())

# 크기 순으로 정리
max_num = max(a,b,c)
min_num = min(a,b,c)
middle_num = a+b+c - max_num - min_num

# 크기 보고 삼각형 되는지
s = 0
if middle_num + min_num > max_num:
    s = max_num + middle_num + min_num
else: # 크기가 더 작거나 같음
    s = 2*(middle_num + min_num) - 1

print(s)
