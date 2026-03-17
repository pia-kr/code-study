# n,m 입력받기
n,m = map(int, input().split())
# 보드 모양 입력받기
board = []
min_count = 64
for _ in range(n):
    board.append(list(input()))


for x in range(n-7):
    for y in range(m-7):
        count = 0
        count_b = 0
        count_w = 0
        for i in range(x,x+8):
            for j in range(y,y+8):
                # B로 시작한 경우 고려
                if (i-x+j-y)%2 == 0:
                    if board[i][j] !='B':
                        count_b += 1
                # W로 시작한 경우 고려
                    if board[i][j] != 'W':
                        count_w += 1
                else:
                    if board[i][j] != 'W':
                        count_b += 1
                    if board[i][j] != 'B':
                        count_w += 1
        count = min(count_b, count_w)
            
        
        if count < min_count:
            min_count = count
print(min_count)