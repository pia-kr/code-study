import sys
input = sys.stdin.readline
print = sys.stdout.write

count = [0] * 10001
n = int(input())

for _ in range(n):
    count[int(input())] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(str(i) + '\n')