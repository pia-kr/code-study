N,M = map(int, input().split())
a = [0]*N
for i in range(M):
    a_1,a_2,a_3 = map(int, input().split())
    for j in range(a_1-1,a_2):
        a[j] = a_3
for k in range(N):
    print(a[k],end=' ')