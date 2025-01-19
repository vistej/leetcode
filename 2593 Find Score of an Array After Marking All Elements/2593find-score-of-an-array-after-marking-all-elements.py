class Solution:
    def findScore(self, nums: List[int]) -> int:
        x = list(enumerate(nums))
        
        x.sort(key=lambda k: (k[1], k[0]))

        marked = set()

        score = 0
        for i, n in x:
            if i not in marked:
                score += n
                marked.add(i)
                if i - 1 >= 0:
                    marked.add(i - 1)
                if i + 1 < len(nums):
                    marked.add(i + 1)
        
        return score