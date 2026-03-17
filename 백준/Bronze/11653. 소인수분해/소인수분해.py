N = int(input())
i= 2
num = []
while i*i <= N:
    while N%i == 0:
        print(i)
        N = N//i
    i += 1
if N > 1:
    print(N)