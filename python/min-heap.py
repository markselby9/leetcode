__author__ = 'fengchaoyi'


class MinHeap():
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def min_heapify_up(self, x):
        if x == 1: return
        parent = x / 2
        if self.heap[parent] > self.heap[x]:
            self.heap[x], self.heap[parent] = self.heap[parent], self.heap[x]
            self.min_heapify_up(parent)

    def min_heapify_down(self, x):
        left_child = 2 * x
        right_child = 2 * x + 1
        smallest = x
        if left_child <= self.size:
            if self.heap[left_child] < self.heap[x]:
                smallest = left_child
        if right_child <= self.size:
            if self.heap[right_child] < self.heap[smallest]:
                smallest = right_child
        self.heap[x], self.heap[smallest] = self.heap[smallest], self.heap[x]
        if smallest != x:
            self.min_heapify_down(smallest)

    def add(self, value):
        self.heap.append(value)
        self.size += 1
        self.min_heapify_up(len(self.heap) - 1)

    def pop_min(self):
        if self.size == 1:
            print "empty"
            return
        answer = self.heap[1]
        if self.size == 1:
            self.size-=1
            return answer
        self.heap[-1], self.heap[1] = self.heap[1], self.heap[-1]
        self.heap.pop()
        self.size -= 1
        self.min_heapify_down(1)
        return answer

    def print_heap(self):
        print "HEAP:", self.heap
        print "size:", self.size


heap = MinHeap()
heap.add(3)
heap.add(4)
heap.add(5)
heap.add(1)
heap.print_heap()
heap.add(2)
heap.add(7)
heap.add(71)
heap.add(12)
heap.add(-1)
heap.add(-3)
heap.print_heap()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
print heap.pop_min()
