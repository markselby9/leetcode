class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        i = 0
        j = length-1
        while (i<j):
            while (i<j) & (not s[i].isalpha()) & (not s[i].isdigit()):
                i+=1
            while (i<j) & (not s[j].isalpha()) & (not s[j].isdigit()):
                j-=1
            if s[i].lower() != s[j].lower():
                return False

            print s[i], s[j],i,j
            i+=1
            j-=1
        return True

sol = Solution()
print sol.isPalindrome("ab2a")