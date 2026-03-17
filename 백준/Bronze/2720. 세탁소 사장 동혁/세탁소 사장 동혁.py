T = int(input())
T_list = []
for i in range(T):
    T_list.append(int(input()))

for j in T_list:
    Quarter = int(j // 25)
    j %= 25
    Dime = int(j // 10)
    j %= 10
    Nickel = int(j //5)
    j %= 5
    Penny = j
    
    print(Quarter, Dime, Nickel, Penny)
#실수의 나눗셈 연산 시 제대로 안될 수 있으니 정수화 시켜서 하는게 좋음