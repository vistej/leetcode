class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasht = {}

        for i, n in enumerate(nums):
            if n in hasht and n + n == target:
                return [hasht[n][1], i]
            hasht[n] = (target - n, i)
        
        for i in hasht:
            nxt = hasht[i][0]
            if nxt in hasht and hasht[nxt][0] == i and hasht[i][1] != hasht[nxt][1]:
                return [hasht[i][1], hasht[nxt][1]]