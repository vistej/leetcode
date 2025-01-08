class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        def isPrefixAndSuffix(a, b):
            x = len(a)
            y = len(b)
            if x > y:
                return False
            if a == b[:x] and a == b[y - x:]:
                return True

        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                l = len(words[i])
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        
        return res