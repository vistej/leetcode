class MinStack:

    def __init__(self):
        self.m = []
        self.s = []

    def push(self, val: int) -> None:
        self.s.append(val)
        v = val
        if self.m:
            v = min(v, self.m[-1])
        self.m.append(v)
        

    def pop(self) -> None:
        self.s.pop()
        self.m.pop()

        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.m[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()