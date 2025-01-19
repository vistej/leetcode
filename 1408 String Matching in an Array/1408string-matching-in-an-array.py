class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        words.sort(key=lambda x: len(x))
        for i in range(len(words)):
            w = words[i]
            for j in range(len(words) - 1, i, -1):
                if len(w) > len(words[j]):
                    break
                if w in words[j]:
                    res.append(w)
                    break
        
        return res