class Solution:
    def countSubarrays(self, nums: List[int], mink: int, maxK: int) -> int:

        res = 0
        
        wi = li = ri = -1

        for i, num in enumerate(nums) :
            if not mink <= num <= maxK:
                wi = i

            if num == mink:
                li = i

            if num == maxK:
                ri = i

            res += max(0, min(li, ri) - wi)

        return res