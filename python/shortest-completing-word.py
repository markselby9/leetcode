class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        plate = [0 for i in range(26)]
        count = 0
        for c in licensePlate:
            if ord(c) >= 97 and ord(c) <= 122:
                plate[ord(c) - 97] += 1
                count += 1
            if ord(c) >= 65 and ord(c) <= 90:
                plate[ord(c) - 65] += 1
                count += 1

        result = None

        for w in words:
            word = w.lower()
            cplate = plate[:]
            cc = 0
            for c in word:
                if ord(c) >= 97 and ord(c) <= 122:
                    if cplate[ord(c) - 97] > 0: cc += 1
                    cplate[ord(c) - 97] -= 1
            if cc == count:
                if result==None or len(result) > len(word):
                    result = word

        return result

licensePlate = "1s3 456"
words = ["looks", "pest", "stew", "show"]
print Solution().shortestCompletingWord(licensePlate, words)
