class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.res = []
        self.solve(n, 0, [-1 for i in xrange(n)])
        return self.res

    def solve(self, n, currQueenNum, board):
        if currQueenNum == n:
            oneAnswer = [ ['.' for j in xrange(n)] for i in xrange(n) ]
            for i in xrange(n):
                oneAnswer[i][board[i]] = 'Q'
                oneAnswer[i] = ''.join(oneAnswer[i])
            self.res.append(oneAnswer)
            return
        # try to put a Queen in (currQueenNum, 0), (currQueenNum, 1), ..., (currQueenNum, n-1)
        for i in xrange(n):
            if self.isSafe(i, currQueenNum, board):
                board[currQueenNum] = i
                self.solve(n, currQueenNum + 1, board)
    def isSafe(self, i, currQueenNum, board):
        for k in range(currQueenNum):
            if board[k]==i: return False #I was wrong at this place, can't use 'i in board'
            if abs(board[k]-i) == abs(currQueenNum-k):
                return False
        return True

s = Solution()
print s.solveNQueens(4)
