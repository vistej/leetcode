class MyCalendar:

    def __init__(self):
        self.d = {}
        

    def book(self, start: int, end: int) -> bool:
        for k,v in self.d.items():
            if start < k:
                if end > k:
                    return False
            else:
                if start < v:
                    return False
        self.d[start] = end
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)