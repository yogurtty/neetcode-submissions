class MinStack:

    def __init__(self):
        self.minStack = []
        self.mainn = []
        

    def push(self, val: int) -> None:
        self.mainn.append(val)
        if val < self.getMin():
            self.minStack.append(val)
        else:
            self.minStack.append(self.getMin())

        

    def pop(self) -> None:
        self.mainn.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.mainn[-1]
        

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        else:
            return self.mainn[-1]
        
