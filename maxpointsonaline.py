class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
	tmp = []
	l = len(points)
	for i in range(l):
	    for j in range(i, l):
		p = points[i]
		q = points[j]
		if (p.x == q.x):
		    rec = -1
		else:
		    rec = (p.y - q.y) / (p.x - q.x)
		tmp.append(rec)
	tmp.sort()
	print tmp 
	

class Point:
    def __init__(self, a=0, b=0):
	self.x = a
	self.y = b

a = Point(1,1)
b = Point(1,0)
c = Point(0,0)
points = [a,b,c]
s = Solution()
print s.maxPoints(points)

