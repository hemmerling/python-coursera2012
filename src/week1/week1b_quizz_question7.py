#!/usr/bin/env python
import math
# 1/4 n s2 / tan(PI/n). 
# number of sides, n, and the length of each side, s,
# Submit the area of a regular polygon with 
# 7 sides each of length 3 inches. 
# Enter a number (and not the units) 
# with at least four digits of precision 
# after the decimal point. 
n = 7.0
s = 3.0
regular_polygon = 1.0/4.0 * n * s**2 / ( math.tan ( math.pi / n ) )
print regular_polygon

n = 5.0
s = 7.0
regular_polygon = 1.0/4.0 * n * s**2 / ( math.tan ( math.pi / n ) )
print regular_polygon
