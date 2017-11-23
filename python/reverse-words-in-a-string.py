class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse_str = s[-1::-1]
        answer = []
        
        buffer = ""
        for c in reverse_str:
            if c == ' ':
                if buffer == "":
                    continue
                else:
                    answer.append(buffer)
                    buffer = ""
            else:
                buffer = c + buffer
        if buffer!="": answer.append(buffer)
        str = ""
        length = len(answer)
        if length==0: return ""
        for i in range(length-1):
            str += answer[i]+" "
        str += answer[-1]
        return str

sol = Solution()
print sol.reverseWords("helloi world   ")