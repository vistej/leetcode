class AllOne:

    def __init__(self):
        self.d = {}
        self.a = [{}]

    def inc(self, key: str) -> None:
        v = self.d.get(key, 0)
        if v:
            del self.a[v][key]
        self.d[key] = v + 1
        if v + 1 == len(self.a):
            self.a.append({})
        self.a[v+1][key] = 1



    def dec(self, key: str) -> None:
        v = self.d.get(key)
        del self.a[v][key]
        if v - 1:
            self.a[v-1][key] = 1
        self.d[key] -= 1

        

    def getMaxKey(self) -> str:
        i = len(self.a) - 1
        while i > 0:
            if self.a[i].keys():
                return next(iter(self.a[i]))
            i -= 1
        return ''

        

    def getMinKey(self) -> str:
        i = 1
        while i < len(self.a):
            if self.a[i].keys():
                return next(iter(self.a[i]))
            i += 1
        return ''


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()