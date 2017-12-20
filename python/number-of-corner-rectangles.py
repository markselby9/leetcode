class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        result = 0

        c1, c2, r1, r2 = 0, 1, 0, 1

        optionX = []
        optionY = []
        option = []

        for i in range(ROWS):
            row = grid[i]
            for j in range(i):
                ones = self.similarOnes(row, grid[j])
                if ones >= 2:
                    result += (ones * (ones-1))/2
        return result

    def similarOnes(self, row1, row2):
        result = 0
        for i in range(len(row1)):
            if row1[i] == 1 and row2[i] == 1:
                result+=1
        return result

        # while c2 < COLUMNS:
        #     r2 = 0
        #     while r2 < ROWS:
        #         if grid[r2][c2] == 1 and grid[r2][0] == 1 and grid[0][c2] == 1:
        #            option.append((r2, c2))
        #         r2 += 1
        #     c2 += 1
        # print option

grid = [[1, 0, 0, 1, 0],
 [0, 0, 1, 0, 1],
 [0, 0, 0, 1, 0],
 [1, 0, 1, 0, 1]]
print Solution().countCornerRectangles(grid)
print Solution().countCornerRectangles([[1, 1, 1],
 [1, 1, 1],
 [1, 1, 1]])
print Solution().countCornerRectangles([[1, 1, 1, 1]])
