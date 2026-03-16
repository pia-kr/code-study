N = int(input())
dic = {}
for i in range(N):
    key, value = (input().split())
    dic[key] = value
ans = []
for key, value in dic.items():
    if value == "enter":
        ans.append(key)
ans = sorted(ans, reverse = True)
print(*ans)