class Bit:
    # set bit n of x to 1
    def setBit(self, x, n): # last nth bit of number x
        return x | (1 << n)

    def getBit(self, x, n):
        return 1 if (x & (1 << n) != 0) else 0

    def clearBit(self, x, n):
        return

bit = Bit()
print bit.setBit(4, 0)
print bit.getBit(4, 0)