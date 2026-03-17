x = int(input())
y = []*x
for i in range(x):
    a,b = input().split()
    c = '' 
    for j in range(len(b)):
        c = c + b[j]*int(a)
    y.append(c)
    
for i in range(x):
    print(y[i])