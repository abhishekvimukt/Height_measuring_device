import math

def distance():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    
    d = math.sqrt((x2-x1)**2 +(y2-y1)**2)
    
    return d

d1 = distance()
d2 = distance()
length = (d2/d1)*28.4
print('the length is %.1f', length)
