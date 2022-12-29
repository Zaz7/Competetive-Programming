class MinStack(object):

    def __init__(self):
        self.stack= []
        self.MinStack = []        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if len(self.MinStack) == 0:
            self.MinStack.append(val)
        else :
            self.MinStack.append(min(val, self.MinStack[-1]))

    
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.MinStack.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
        
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.MinStack[-1]
