class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 10:
            return []
        resultmap = {}
        result = []
        pos = 0
        while pos <= len(s)-10:
            str = s[pos:pos+10]
            if str in resultmap:
                resultmap[str] +=1
            else:
                resultmap[str] = 1
            pos+=1
        for (k, v) in resultmap.items():
            if v > 1:
                result.append(k)
        return result

    def strToNumber(self, str):
        number_str = ""
        for c in str:
            z=''
            if c == 'A': z = '1'
            if c == 'C': z = '2'
            if c == 'G': z = '3'
            if c == 'T': z = '4'
            number_str += z
        return int(number_str)

sol = Solution()
print sol.findRepeatedDnaSequences("AAAAAAAAAAAAAAAGGGTTT")