# n,k입력
n, k = map(int, input().split())
# n개의 수 입력받기
num = list(map(int, input().split()))
# 내림차순 정렬
num.sort(reverse=True)
# k번째 수 출력 -> 커트라인 마지막
print(num[k-1])