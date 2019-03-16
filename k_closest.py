"""
Definition for a point.
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param points: a list of points
    @param origin: a point
    @param k: An integer
    @return: the k closest points
    """
    def compare(self, point1, point2):
        if (point1.x-self.origin.x)**2+(point1.y-self.origin.y)**2 < (point2.x-self.origin.x)**2+(point2.y-self.origin.y)**2:
            print 1, point1.x, point1.y, ' < ', point2.x, point2.y
            return True 
        elif (point1.x-self.origin.x)**2+(point1.y-self.origin.y)**2 == (point2.x-self.origin.x)**2+(point2.y-self.origin.y)**2:
            if point1.x < point2.x:
                print 2, point1.x, point1.y, ' < ', point2.x, point2.y
                return True  
            elif point1.x == point2.x:
                return point1.y < point2.y
            else:
                return False 
        else:
            return False 
        
    def kClosest(self, points, origin, k):
        # write your code here
        self.origin = Point(origin[0], origin[1])
        points = [Point(x[0], x[1]) for x in points]
        points = sorted(points, cmp=self.compare)
        for i in points:
            print i.x, i.y
        return points[:k]


points = [[4,6],[4,6],[4,6],[-4,-6]]
origin = [0,0]
k = 3
s = Solution()
result = s.kClosest(points, origin, k)
