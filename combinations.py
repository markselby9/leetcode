__author__ = 'fengchaoyi'
class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        if n<k or n<=0 or k<=0:
            return []
        if n==k:
            return [x+1 for x in xrange(n)]

        answer = [[x+1] for x in range(n)]
        if k==1:
            return answer
        ans = self.combine2(n, k, answer)
        return ans

    def combine2(self, n, k, last):
        if k==1:
            return last
        current = []
        i=0
        while i < len(last):
            lastitem = last[i]
            j = 0
            while j < n:
                nowitem = list(lastitem)
                if not (j+1) in nowitem:
                    nowitem.append(j+1)
                    nowitem.sort()
                    if not nowitem in current:
                        current.append(nowitem)
                j+=1
            i+=1
        return self.combine2(n, k-1, current)

s = Solution()
print s.combine(13,10)
