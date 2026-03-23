n,m = map(int, input().split())
d= []
for i in range (n):
    d.append(list(map(int, input())))
# 각 점은 오른쪽 아래 꼭짓점으로 보고 왼쪽, 오른쪽, 위쪽 값 중 작은거 + 1

for i in range(n):
    for j in range(m):
        if d[i][j] == 1:
    #수정1: 이렇게 하면 i j 가 0일때 -1반, 제일 뒤의 값을 불러옴
    #d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
         # 조건 추가
            if i > 0 and j > 0 :
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1

# 최대의 값 찾기
max_d = d[0][0]
for i in range(len(d)):
    for j in range(len(d[i])):
        if d[i][j] > max_d:
            max_d = d[i][j]
# 출력은 넓이니            
print(max_d*max_d)