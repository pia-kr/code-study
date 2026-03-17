x = int(input()) #x는 몇 번 받을지

a = [0,0,0,0,0,0,0,0,0,0]

for i in range(x):
    y = input()
    a[i] = y[0]+y[-1]
    
    
for j in range(x):
    print(a[j])