import math
point = [4,7]
circle_point = [2,9]
circle_radius = 2
p0 = point
p1 = circle_point
distance= math.sqrt( (p0[0]-p1[0])**2+(p0[1]-p1[1])**2 )
distance2 = distance - 2
print round(distance2,4)