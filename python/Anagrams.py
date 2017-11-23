class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        result = {}
        dic={}
        if len(strs)<2:
            return []
        for str in strs:
            sortedstr = ''.join(sorted(str))
            dic[sortedstr]=[str] if sortedstr not in dic else dic[sortedstr]+[str]
        for (k,v) in dic.items():
            if len(v)>1:
                result[k]=v
        ans = []
        for (k,v) in result.items():
            # + different from append
            ans+=v
        return ans