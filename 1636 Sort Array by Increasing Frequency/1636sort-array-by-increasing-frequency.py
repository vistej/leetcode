class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1
        
        k = [(j, i) for i,j in d.items()]
        k.sort(key=lambda x: (x[0], -x[1]))
        r = []
        for m,n in k:
            while m:
                r.append(n)
                m -= 1

        return r