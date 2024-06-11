class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        s = sum(apple)
        capacity.sort(reverse=True)
        c = 0
        for i in capacity:
            s -= i
            c += 1
            if s <= 0:
                break
        return c