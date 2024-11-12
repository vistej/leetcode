class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key=lambda x: x[1], reverse=True)
        res = []

        for q in queries:
            ans = 0
            for p,b in items:
                if p <= q:
                    ans = b
                    break

            res.append(ans)
        
        return res
            