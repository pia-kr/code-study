numbers = []
for i in range(5):
    numbers.append(int(input()))
# 오름차순 정렬
numbers.sort()
mean = sum(numbers) // len(numbers)
mideum = numbers[len(numbers) // 2]
print(mean)
print(mideum)
