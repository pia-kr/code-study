x = int(input())
y = list(map(int, input()))
a = 0
for i in range(x):
    a = a + y[i]
print(a)