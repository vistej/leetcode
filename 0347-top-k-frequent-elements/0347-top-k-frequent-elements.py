class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = defaultdict(int)
        for n in nums:
            obj[n] += 1
        lst = list(obj.items())
        lst.sort(key=lambda x: x[1], reverse=True)
        res = []
        i = 0
        while i < k:
            res.append(lst[i][0])
            i += 1
        
        return res