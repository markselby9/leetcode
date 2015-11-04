# coding=utf-8
# Question:
# Design and implement a TwoSum class. It should support the following operations: add and find.
# add(input) – Add the number input to an internal data structure.
# find(value) – Find if there exists any pair of numbers which sum is equal to the value.

class TwoSum:
    def __init__(self):
        self.map = {}

    def add(self, x):
        if x in self.map:
            self.map[x] += 1
        else:
            self.map[x] = 1

    def find(self, value):
        for key in self.map.keys():
            if (value-key) in self.map:
                if key == value-key:
                    if self.map[key] > 1: return True
                    return False
                else:
                    return True
        return False

sol = TwoSum()
sol.add(1)
sol.add(1)
sol.add(1)
sol.add(5)
sol.add(5)
sol.add(5)
print sol.find(2)