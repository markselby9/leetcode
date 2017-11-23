from collections import OrderedDict
class LRUCache:
    cache = OrderedDict()
    capacity = 0

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    # @return an integer
    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.cache:
            del self.cache[key]
            self.cache[key] = value
            return
        if len(self.cache) == self.capacity:
            self.cache.popitem(False)
        self.cache[key] = value
        return
# 2,[set(2,1),set(1,1),set(2,3),set(4,1),get(1),get(2)]
sol = LRUCache(2)
sol.set(2,1)
sol.set(1,1)
sol.set(2,3)
sol.set(4,1)
print sol.get(1)
print sol.get(2)