class NumberContainers:

    def __init__(self):
        self.ids = defaultdict(int)
        self.numbers = defaultdict(list)

    def change(self, index: int, number: int) -> None:
        if self.ids[index]:
            if self.ids[index] == number:
                return
            temp = []
            n = self.ids[index]
            while self.numbers[n][0] != index:
                temp.append(heapq.heappop(self.numbers[n]))
            heapq.heappop(self.numbers[n])
            for t in temp:
                heapq.heappush(self.numbers[n], t)
        heapq.heappush(self.numbers[number], index)
        self.ids[index] = number
        

    def find(self, number: int) -> int:
        if not self.numbers[number]:
            return -1
        else:
            return self.numbers[number][0]
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)