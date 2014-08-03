class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        if len(num) < 4: return []
        dictionary = {}
        result = set()
        num.sort()
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                if ((num[i]+num[j]) in dictionary):
                    dictionary[num[i]+num[j]].append((i, j))
                else:
                    dictionary[num[i]+num[j]] = [(i, j)]
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                S = target-num[i]-num[j]
                if (S in dictionary):
                    pairlist = dictionary[S]
                    for pair in pairlist:
                        if (pair[0]>j):
                            result.add((num[i], num[j], num[pair[0]], num[pair[1]]))

        return [list(i) for i in result]