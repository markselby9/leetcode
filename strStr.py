class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_hay = len(haystack)
        len_nee = len(needle)
        if len_nee == 0:
            return 0
        if len_nee > len_hay:
            return -1
        i = 0
        j = 0
        while i < len_hay:
            i_start = i
            while (j < len_nee) & (i_start < len_hay):
                print i_start, j
                if haystack[i_start] != needle[j]:
                    break
                if j == len_nee-1:
                    return i
                if i_start+j == len_hay:
                    return -1
                j+=1
                i_start+=1
            j=0
            i+=1
        return -1

sol = Solution()
print sol.strStr("mississippi", "issippi")