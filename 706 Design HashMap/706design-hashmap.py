class MyHashMap:
    def __init__(self):
        self.hashmap = []
        
    def findIndex(self, key):
            for i, v in enumerate(self.hashmap):
                if v[0] == key:
                    return i
            return -1

    def put(self, key: int, value: int) -> None:
        key_index = self.findIndex(key)
        if key_index == -1:
            self.hashmap.append([key, value])
        else:
            self.hashmap[key_index][1] = value

    def get(self, key: int) -> int:
        key_index = self.findIndex(key)
        if key_index != -1:
            return self.hashmap[key_index][1]
        else:
            return key_index
        

    def remove(self, key: int) -> None:
        key_index = self.findIndex(key)
        if key_index != -1:
            del self.hashmap[key_index]
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)