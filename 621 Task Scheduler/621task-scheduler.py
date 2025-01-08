class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = list(Counter(tasks).items())
        counts.sort(key=lambda x: x[1], reverse=True)
        counts = [[i + 1, x, y] for i,(x,y) in enumerate(counts)]
        res = 0

        heapq.heapify(counts)

        while counts:
            x = heapq.heappop(counts)
            if x[0]  <= res:
                res += 1
            else:
                res = x[0]
            
            x[2] -= 1
            if x[2]:
                k = 1 if n > 1 else 0
                x[0] = res + n + k
                heapq.heappush(counts, x)
            print(counts)
        return res
