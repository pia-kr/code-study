ran = []
for _ in range(3):
    ran.append(int(input()))
sum = 0
count = 0
for i in range(3):
    sum += ran[i]
if sum != 180:
    print("Error")
else:
    if ran[0] == ran[1] == ran[2]:
        print("Equilateral")

    elif ran[0] == ran[1] or ran[0] == ran[2] or ran[1] == ran[2]:
        print("Isosceles")
    else:
        print("Scalene")