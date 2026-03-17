x, y = input().split()

reveresd_x = int(str(x)[::-1])
reveresd_y = int(str(y)[::-1])

if reveresd_x > reveresd_y  :
    print(reveresd_x)

else:
    print(reveresd_y)