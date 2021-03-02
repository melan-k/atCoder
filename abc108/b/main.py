import math
x1, y1, x2, y2 = map(int, input().split())
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
if x2 - x1 == 0:
    slope = 1
    r_slope = 0
else:
    slope = (y2 - y1) / (x2 - x1)
    r_slope = (x2 - x1) / (y2 - y1)

# 地点2から地点3への傾きは、地点2から地点1への傾きの逆数
y3 = distance * r_slope + y2
print(y3)