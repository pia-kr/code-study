while(True):
    m = []
    sum = 0
    n = int(input())
    if n == -1:
        break
    for i in range(1,n):
        if n%i == 0:
            m.append(i)
    for j in m:
        sum += int(j)
    if sum == n:
        print(f"{n} = " + " + ".join(map(str, m)))
    else:
        print(f"{n} is NOT perfect.")