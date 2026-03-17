N,M = map(int, input().split())
a =[0]*N
for i in range(N):
    a[i] = i+1
for j in range(M):
    a_1,a_2= map(int, input().split())
    x = a[a_1-1]
    a[a_1-1] = a[a_2-1]
    a[a_2-1] = x
for k in range(N):
    print(a[k],end=' ')