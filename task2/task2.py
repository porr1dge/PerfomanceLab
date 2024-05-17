import sys
import math

circleF = open(sys.argv[1])
pointsF = open(sys.argv[2])
l1 = [line.strip() for line in circleF]
l2 = [line.strip() for line in pointsF]

x, y = l1[0].split(' ')
x = float(x)
y = float(y)
r = float(l1[1])

for i in l2:
    xp, yp = i.split(' ')
    xp = float(xp)
    yp = float(yp)
    c = math.sqrt((x - xp) ** 2 + (y - yp) ** 2)
    if c == r:
        print(0)
    elif c < r:
        print(1)
    else:
        print(2) 

circleF.close()
pointsF.close()



