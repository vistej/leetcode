class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        counts = Counter(s)

        arr = []

        for c, i in counts.items():
            arr.append([-ord(c), c, i])

        heapq.heapify(arr)

        res = ''

        while arr:
            obj = heapq.heappop(arr)
            if obj[2] > repeatLimit:
                res += obj[1] * repeatLimit
                obj[2] -= repeatLimit
                if arr:
                    obj2 = heapq.heappop(arr)
                    res += obj2[1]
                    if obj2[2] > 1:
                        obj2[2] -= 1
                        heapq.heappush(arr, obj2)
                    heapq.heappush(arr, obj)
                else:
                    break
            else:
                res += obj[1] * obj[2]
        
        return res