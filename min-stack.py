class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_store = []
        self.min = ''

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if self.min == '':
            self.min = x
            self.min_store.append(self.min)
        else:
            if x <= self.min:
                self.min_store.append(x)
                self.min = x
        # print self.min

    def pop(self):
        """
        :rtype: nothing
        """
        ans = self.stack.pop()
        if self.min_store[-1] == ans:
            self.min_store.pop()
            if len(self.min_store)!=0:
                self.min = self.min_store[-1]
            else:
                self.min = ''
        return ans

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_store[-1]


min_stack = MinStack()
min_stack.push(395)
min_stack.push(276)
min_stack.push(29)
min_stack.push(-482)
min_stack.pop()
min_stack.push(-108)
min_stack.push(-251)
print min_stack.getMin()