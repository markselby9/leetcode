class Solution(object):
    def helper(self, grid):
        N = len(grid) # j
        M = len(grid[0]) # i
        record = [[0 for i in range(M)] for j in range(N)]
        path = [[0 for i in range(M)] for j in range(N)]  # 1 for right, 2 for down, 3 for left, 4 for up
        tentative = []

        for i in range(N):
            for j in range(M):
                if grid[i][j] == -1:
                    record[i][j] = -1
                elif i == 0 and j == 0:
                    record[i][j] = grid[i][j]
                elif i == 0:
                    if record[i][j - 1] == -1:
                        record[i][j] = -1
                    else:
                        record[i][j] = record[i][j - 1] + grid[i][j]
                        path[i][j] = 2
                elif j == 0:
                    if record[i - 1][j] == -1:
                        record[i][j] = -1
                    else:
                        record[i][j] = record[i - 1][j] + grid[i][j]
                        path[i][j] = 1
                else:
                    if record[i - 1][j] == -1 and record[i][j - 1] == -1:
                        record[i][j] = -1
                    elif record[i - 1][j] >= record[i][j - 1]:  # TODO
                        record[i][j] = record[i - 1][j] + grid[i][j]
                        path[i][j] = 1
                    else:
                        record[i][j] = record[i][j - 1] + grid[i][j]
                        path[i][j] = 2
        current_cherry = record[N - 1][M - 1]
        if current_cherry <= 0: return 0

        i, j = N - 1, M - 1
        while i != 0 or j != 0:
            grid[i][j] = 0  # clear
            if path[i][j] == 1:
                i -= 1
            else:
                j -= 1
        grid[0][0] = 0

        # return
        i, j = M - 1, N - 1
        record = [[0 for i in range(M)] for j in range(N)]
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if grid[i][j] == -1:
                    record[i][j] = 0
                elif i == N - 1 and j == M - 1:
                    record[i][j] = grid[i][j]
                elif i == N - 1:
                    if record[i][j + 1] == -1:
                        record[i][j] = -1
                    else:
                        record[i][j] = record[i][j + 1] + grid[i][j]
                elif j == M - 1:
                    if record[i + 1][j] == -1:
                        record[i][j] = -1
                    else:
                        record[i][j] = record[i + 1][j] + grid[i][j]
                else:
                    if record[i + 1][j] == -1 and record[i][j + 1] == -1:
                        record[i][j] = -1
                    else:
                        record[i][j] = max(record[i + 1][j], record[i][j + 1]) + grid[i][j]
        current_cherry += record[0][0]
        return current_cherry

    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        N = len(grid) # j
        record = [[0 for i in range(N+1)] for j in range(N+1)]
        answer = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                child_grid = [[0 for ii in range(i)] for jj in range(j)]
                for ii in range(i):
                    for jj in range(j):
                        child_grid[jj][ii] = grid[jj][ii]
                print child_grid, self.helper(child_grid)
                answer = max(answer, self.helper(child_grid))
        return answer


grid = [[0, 1, -1],
        [1, 0, -1],
        [1, 1, 1]]
# print Solution().cherryPickup(grid) # 5
grid = [[1, 1, -1], [1, -1, 1], [-1, 1, 1]]
# print Solution().cherryPickup(grid)
# print Solution().cherryPickup([[1]])
print Solution().cherryPickup([[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]) # 15
