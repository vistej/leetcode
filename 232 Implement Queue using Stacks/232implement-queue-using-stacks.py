class MyQueue:

    def __init__(self):
        self.ra = []
        self.rb = []

    def push(self, x: int) -> None:
        self.ra.append(x)

    def pop(self) -> int:
        while len(self.ra):
            a = self.ra.pop()
            self.rb.append(a)
        b = self.rb.pop()
        while len(self.rb):
            a = self.rb.pop()
            self.ra.append(a)
        return b


    def peek(self) -> int:
        return self.ra[0]
        

    def empty(self) -> bool:
        return len(self.ra) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()