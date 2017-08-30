'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        self.minItem = [] # 维护一个和原栈大小相同的，但是保存的是当前最小元素的辅助栈

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.items.append(x)
        if len(self.minItem) == 0 or self.minItem[-1] > x:
            self.minItem.append(x)
        else:
            self.minItem.append(self.minItem[-1])
        

    def pop(self):
        """
        :rtype: void
        """
        self.items.pop()
        self.minItem.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.items[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minItem[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()