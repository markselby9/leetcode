class Heap(object):
    # heap_array = []
    # def __init__(self, size):
    #     self.heap_array = [0]*size

    def max_heapify(self, A, i):
        left_child = 2*i
        right_child = 2*i+1
        largest = i
        if left_child < len(A):
            if A[left_child] > A[i]:
                largest = left_child
        if right_child < len(A):
            if A[right_child] > A[largest]:
                largest = right_child
        if largest != i:
            #switch largest
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest)

    def build_max_heap(self, A):
        size = len(A)
        for i in range(size/2, -1, -1):
            self.max_heapify(A, i)

    def extract_max(self, A):
        A[0], A[len(A)-1] = A[len(A)-1], A[0]
        max = A.pop(len(A)-1)
        self.max_heapify(A, 0)
        return max

    def sort(self, array):
        self.build_max_heap(array)
        result = []
        print array
        while len(array) > 0:
            result.insert(0, self.extract_max(array))
        return result

heap = Heap()
array = [5,4,3,2,1,6,7,8,9]
heap.build_max_heap(array)
print heap.sort(array)