# N 입력받기
N = int(input())
# 리스트에 N개의 정수 입력받기
numbers = list(map(int, input().split()))
# 생각 : 중복 제거 후 오름차순으로 인덱스 저장된 배열 생성
seted_numbers = set(numbers)
seted_numbers = sorted(seted_numbers)
'''
# 생각: 인덱스 추가된 배열에서 그 값에 해당하는 인덱스로 넣기(인덱스로 보면 0~N 되기에)
num_with_index = []
for i in range(len(seted_numbers)):
    num_with_index.append((seted_numbers[i], i))

for i in range(len(numbers)):
    for j in num_with_index:
         if numbers[i] == j[0]:
            numbers[i] = j[1]'''
# 수정: 시간초과 -> 딕셔너리로 생각해서 호출로 바꾸기
# i v 형태 아니고 v i 형태인 이유는 v 값으로 i를 호출하기 위해
dic_num = {v: i for i, v in enumerate(seted_numbers)}

# 출력 : 키 값이 진짜 숫자 , value값이 그에 해당하는 인덱스
for key in numbers:
    print(dic_num[key], end=' ')
