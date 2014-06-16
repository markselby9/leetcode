class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
	return 0

class Point:
    def __init__(self, a=0, b=0):
	self.x = a
	self.y = b

a = Point (1,1)
points = [a]
s = Solution()
print a.x, a.y
print s.maxPoints(points)

