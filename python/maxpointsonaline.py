# Solution: use python dictionary to keep the result, pay attention to the same points
# and the slope should be float

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
	length = len(points)
	if length < 2:
	    return length
	result = 0
	for i in range(length):
	    samepoint = 0 
	    slope={'inf':0}
	    for j in range(length):
		p = points[i]
		q = points[j]
		if (p.x == q.x):
		    if (p.y == q.y):
			samepoint+=1
		    else:
			slope['inf']+=1
		else:
		    it = 1.0 * (p.y - q.y) / (p.x - q.x)
		    if it in slope: slope[it]+=1
		    else: slope[it]=1
	    result = max(result, max(slope.values())+samepoint)
#            print slope
	return result


class Point:
    def __init__(self, a=0, b=0):
	self.x = a
	self.y = b

points = [Point(84,250),Point(0,0),Point(1,0),Point(0,-70),Point(0,-70),Point(1,-1),Point(21,10),Point(42,90),Point(-42,-230)]
s = Solution()
print s.maxPoints(points)

