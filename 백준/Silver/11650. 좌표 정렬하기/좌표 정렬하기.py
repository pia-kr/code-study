"""# N 입력받기
N = int(input())
# x좌표 y좌표 쌍으로 입력받기
coordinate = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append((x, y))

# x좌표 기준으로 정렬
coordinate.sort(key = lambda x: x[0])
# x좌표가 같을 때 y좌표 기준으로 정렬
for i in range(N-1):
    if coordinate[i][0] == coordinate[i+1][0]: 
        if coordinate[i][1] > coordinate[i+1][1]:
            coordinate[i], coordinate[i+1] = coordinate[i+1], coordinate[i] 
for i in range(N):
    print(*coordinate[i])

# 추가 coordinate.sort() 하면 자동으로 x y 기준으로 정렬됨"""

N = int(input())
coordinate = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append((x, y))
coordinate.sort()
for i in range(N):
    print(*coordinate[i])