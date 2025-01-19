class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        d = {v: 1 for v in nums}
        streak = 0
        max_streak = -1
        for n in nums:
            while n in d:
                streak += 1
                n *= n
            if streak > 1:
                max_streak = max(streak, max_streak)
            streak = 0
        
        return max_streak