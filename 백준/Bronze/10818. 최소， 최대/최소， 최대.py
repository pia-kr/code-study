a = int(input())
a_list = list(map(int, input().split()))

a_list.sort()
print(a_list[0], a_list[-1])