a = int(input())
a_list = list(map(int, input().split()))
b = int(input())
count = 0
for i in range(a):
    if b == a_list[i]:
        count +=1
print(count)