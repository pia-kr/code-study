# N 입력받기
N = int(input())
# 문자들 입력받기
chars = []
for _ in range(N):
    chars.append(input())
# 중복 제거 -> set
chars = list(set(chars))
# 길이순으로 정렬 -> 사전순
chars.sort(key=lambda x: (len(x), x))
for i in range(len(chars)):
    print(chars[i])