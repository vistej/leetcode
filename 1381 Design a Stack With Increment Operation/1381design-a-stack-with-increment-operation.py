class CustomStack:

    def __init__(self, maxSize: int):
        self.a = []
        self.l = maxSize

    def push(self, x: int) -> None:
        if len(self.a) < self.l:
            self.a.append(x)
        

    def pop(self) -> int:
        x = self.a.pop() if self.a else -1
        return x

    def increment(self, k: int, val: int) -> None:
        i = 0
        while i < k and i < len(self.a):
            self.a[i] += val
            i += 1
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)