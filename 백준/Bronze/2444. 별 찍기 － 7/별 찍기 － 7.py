x = int(input())

for i in range(x):
    print(" " * (x-(i+1)), end='')
    print("*" * (2*i+1))
    
for j in range(x-1,0,-1):
    print(" " * (x-j), end='')
    print("*" * (2*j-1))