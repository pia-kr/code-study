N = int(input())

numbers = list(map(int, input().split()))
list_sosu = []
for i in numbers:
    a = 0
    for j in range(1, i+1):
        if i % j == 0:
            a += 1
    if a == 2:
        list_sosu.append(i)
print(len(list_sosu))
            