N = int(input())
sum = 1
i = 1
while True:
    sum += (i-1)*6
    if sum >= N:
        print(i)
        break
    else:
        i += 1