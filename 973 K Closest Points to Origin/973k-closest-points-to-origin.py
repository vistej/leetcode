class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = [(p[0]**2 + p[1]**2, p) for p in points]
        res = []

        heapq.heapify(arr)

        for _ in range(k):
            res.append(heapq.heappop(arr)[1])

        return res        