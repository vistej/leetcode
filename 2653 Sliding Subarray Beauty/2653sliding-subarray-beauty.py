class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
         
        la = [0 for _ in range(101)]
        r = []

        for i in range(len(nums)):
            la[nums[i] + 50] += 1

            if i >= k - 1:
                s = 0
                j = 0
                while s < x:
                    s += la[j]
                    j += 1
                a = j - 50 - 1
                r.append(a if a < 0 else 0)

                la[nums[i - k + 1] + 50] -= 1
        return r

