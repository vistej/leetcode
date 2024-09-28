from collections import deque
class MyCircularDeque:

    def __init__(self, k: int):
        self.l = k
        self.d = deque()

    def insertFront(self, value: int) -> bool:
        if len(self.d) < self.l:
            self.d.appendleft(value)
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        if len(self.d) < self.l:
            self.d.append(value)
            return True
        else:
            return False

    def deleteFront(self) -> bool:
        if self.d:
            self.d.popleft()
            return True
        else:
            return False

    def deleteLast(self) -> bool:
        if self.d:
            self.d.pop()
            return True
        else:
            return False
        

    def getFront(self) -> int:
        return self.d[0] if self.d else -1
        

    def getRear(self) -> int:
        return self.d[-1] if self.d else -1
        

    def isEmpty(self) -> bool:
        return not bool(self.d)
        

    def isFull(self) -> bool:
        return len(self.d) == self.l
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()