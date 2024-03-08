class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        maxv = []
        counts = {}
        for num in nums:
            counts[num] = 1 + (counts[num] if num in counts else 0)
            if len(maxv) == 0 or counts[num] > counts[maxv[0]]:
                maxv = [num]
            elif counts[num] == counts[maxv[0]]:
                if num != maxv[0]:
                    maxv.append(num)
                else:
                    maxv = [num]
        res = 0
        for v in maxv:
            res = res + counts[v]
        return res  

            
        