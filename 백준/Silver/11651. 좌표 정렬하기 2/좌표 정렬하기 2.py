# N 입력받기
N = int(input())
coordinate = []
# 좌표들 입력받기
for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append((x, y))
# y x 순으로 정렬하기 -> 기본 sort는 x[0] x[1] 순
coordinate.sort(key = lambda x:(x[1], x[0]))
for i in range(N):
    print(*coordinate[i])