class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        c = 0
        s = 0
        for a, b in customers:
            c = max(a, c) + b
            s += c - a
        return s / len(customers)