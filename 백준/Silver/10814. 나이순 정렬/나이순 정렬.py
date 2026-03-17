# N 입력받기
N = int(input())
# 나이, 이름 입력받기
people = []
for i in range(N):
    # 주의 : 이름은 str, 나이는 int 기에 나중에 int 취하기 귀찮으면 미리 넣어서 받기 
    age, name = input().split()
    people.append((int(age), name, i))
people.sort(key=lambda x: (x[0], x[2]))
# people list에 2번 index에 가입 순을 넣어놨기에 print(people) 안하기
for j in people:
    print(j[0], j[1])