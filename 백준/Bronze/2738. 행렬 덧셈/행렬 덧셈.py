x,y = map(int, input().split())


a = [list(map(int, input().split())) for _ in range(x)]
b = [list(map(int, input().split())) for _ in range(x)]
c = [[0]*y]*x

for i in range(x):
    c[i] = [x+y for x,y in zip(a[i],b[i])]
        
for i in range(x):
    for j in range(y):
        print(c[i][j], end =' ')
    print("\n", end='')