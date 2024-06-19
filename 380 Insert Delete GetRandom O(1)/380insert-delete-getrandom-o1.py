class RandomizedSet:

    def __init__(self):
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = val
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            del self.d[val]
            return True
        return False

    def getRandom(self) -> int:
        a = list(self.d.keys())
        return random.choice(a)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()