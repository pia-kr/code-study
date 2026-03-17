n = int(input())
answer = []

for i in range(n):
    a = input()
    count = 0
    for j in a:
        if j == '(':
            count += 1
        elif j == ')':
            count -= 1
        if count < 0:
            answer.append('NO')
            break    
    if count == 0:
        answer.append('YES')
    elif count > 0:
        answer.append('NO')
    
for i in answer:
    print(i)