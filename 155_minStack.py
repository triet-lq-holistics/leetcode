class MinStack:

    def __init__(self):
        self.stack = []
        
    @property
    def minVal(self):
        return self.stack[-1][1] 

    def push(self, val: int) -> None:
        minVal = min(self.minVal, val) if self.stack else val
        self.stack.append((val, minVal))

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.minVal