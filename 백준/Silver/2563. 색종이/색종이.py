n = int(input())
square = [[0] * 100 for _ in range(100)]
answer = 0
for _ in range(n):
    y,x = map(int, input().split())
    
    for i in range(x,x+10):
        for j in range(y,y+10):
            square[i][j] = 1
            
            
for i in range(100):
    for j in range(100):
        if square[i][j] == 1:
            answer += 1
            
print(answer)