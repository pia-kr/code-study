##풀이 : 리스트에 리스트를 입력받게 하여 행렬 구하기
a = []
for i in range(9):
    a.append(list(map(int, input().split())))
x = 0
y = 0
for i in range(9):
    for j in range(9):
        if a[i][j] > a[x][y]:
            x = i
            y = j   
print(a[x][y])
##인덱스이니 답은 1 증가시켜서 출력하기
print(x+1,y+1)