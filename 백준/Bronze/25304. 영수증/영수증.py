a = int(input())
b = int(input())
c = 0
for i in range(b):
   d,e = map(int, input().split())
   c += d*e
if a == c:
   print('Yes')
else:
   print('No')