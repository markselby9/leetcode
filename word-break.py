class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        length = len(s)
        result = [False]*length
        if s in wordDict: return True

        for i in range(length):
            for j in range(i+1, length+1):
                # print i,j,s[i:j]
                if i==0:
                    if s[i:j] in wordDict:
                        result[j-1] = True
                else:
                    if result[i-1]==True and s[i:j] in wordDict:
                        result[j-1] = True
        # print result
        return result[-1]

sol = Solution()
print sol.wordBreak("helloworld", ["hello", "world"])
print sol.wordBreak("goalspecialgoal", ["go","goal","goals","special"])
print sol.wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"])
print sol.wordBreak("ab", ["a","b"])