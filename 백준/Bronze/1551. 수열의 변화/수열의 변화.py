# 입력받기
n, k = map(int, input().split())
arr = list(map(int, input().split(',')))
new_arr = []
# k 번 반복하기
for i in range(k):
    new_arr = []
    for j in range(len(arr)-1):
        new_arr.append(arr[j+1]-arr[j])
    arr = new_arr
# 추가 k == 0 인 경우
if k == 0:
    new_arr = arr
print(*new_arr, sep=',')