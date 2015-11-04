__author__ = 'fengchaoyi'


class Sort(object):
    def quicksort(self, array):
        if len(array) <= 1: return array
        pivot = array[0]
        less = []
        more = []
        for i in range(1, len(array)):
            if array[i] < pivot:
                less.append(array[i])
            else:
                more.append(array[i])
        return self.quicksort(less) + [pivot] + self.quicksort(more)

    def mergesort(self, array):
        length = len(array)
        if length <= 1: return array
        left = array[:length/2]
        right = array[length/2:]
        left = self.mergesort(left)
        right = self.mergesort(right)
        return self.merge(left, right)

    def merge(self, left, right):
        if len(left) == 0: return right
        if len(right) == 0: return left
        result = []
        l=0
        r=0
        while (l < len(left)) & (r < len(right)):
            if left[l] <= right[r]:
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
        if l != len(left):
            result+= left
        if r != len(right):
            result+=right
        return result

    def insertionsort(self, array):
        if len(array)<=1: return array
        i = 1
        while i < len(array):
            for j in range(i, 0, -1):
                if array[j-1] > array[j]:
                    array[j-1], array[j]=array[j],array[j-1]
            i+=1
        return array


print Sort().quicksort([1, 2, 3, 4, 5, -1])
print Sort().mergesort([6,5,4,3,2,1,-2,-3])
print Sort().insertionsort([6,5,4,3,2,1,-2,-3])