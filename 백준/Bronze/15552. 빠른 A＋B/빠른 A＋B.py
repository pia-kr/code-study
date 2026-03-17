import sys
a = int(input())
for _ in range(a):
    b,c = map(int, sys.stdin.readline().split())
    print(b+c)