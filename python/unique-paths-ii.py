class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        pathGrid = [[1 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    pathGrid[i][j] = 0
                else:
                    if i==0 and j>0:
                        pathGrid[0][j] = pathGrid[0][j-1]
                    if j==0 and i>0:
                        pathGrid[i][0] = pathGrid[i-1][0]
                    if i>0 and j>0:
                        pathGrid[i][j] = pathGrid[i-1][j] + pathGrid[i][j-1]
        print pathGrid
        return pathGrid[m-1][n-1]

print Solution().uniquePathsWithObstacles([[1,0]])