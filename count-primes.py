class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0: return 0
        count = 0
        arr = [True for i in range(2, n)] #[2,3,...,n-1]

        i = 0
        while i+2<n:
            if not arr[i]:
                i+=1
            elif self.isPrime(i+2):
                #set corresponding -1
                multi = 2
                count+=1
                while multi*(i+2)<n:
                    arr[multi*(i+2)-2]=False
                    multi+=1
                i+=1
            else:
                i+=1

        # print arr
        return count

    def isPrime(self, n):
        if n<2: return False
        i = 2
        while i*i<=n:
            if n % i == 0:
                return False
            i+=1
        return True

print Solution().countPrimes(1500000)