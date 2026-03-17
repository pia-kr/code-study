N, M = map(int, input().split())
# 기준
a_list = []
# 확인할 거
b_list = []
for i in range(N):
    a_list.append(input())
for j in range(M):
    b_list.append(input())
count = 0
for j in range(M):
    if b_list[j] in a_list:
        count += 1
print(count)