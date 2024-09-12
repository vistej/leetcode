class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        c = 0
        def check(a, b):
            for i in a:
                if i not in b:
                    return 0
            return 1
        for w in words:
            c += check(w, allowed)
        
        return c