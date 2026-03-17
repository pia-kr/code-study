# 각 자리 수들을 리스트로 입력받기
num = list(map(int, input()))
# 각 자리 수 정렬
num.sort(reverse=True)

print(''.join(map(str, num)))
#  join 함수는 문자열만 합칠 수 있기에 str 필요