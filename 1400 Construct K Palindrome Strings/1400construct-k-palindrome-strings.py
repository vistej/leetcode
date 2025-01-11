class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        counts = Counter(list(s))

        odds = 0

        for _, v in counts.items():
            if v % 2:
                odds += 1
            if odds > k:
                return False
        
        return True