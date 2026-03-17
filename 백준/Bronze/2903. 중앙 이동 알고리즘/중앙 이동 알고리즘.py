N = int(input())
count = 2
for i in range(N):
    count += count-1
count *=count
print(count)
