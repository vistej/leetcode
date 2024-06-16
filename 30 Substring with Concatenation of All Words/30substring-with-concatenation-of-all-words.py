from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        wc = defaultdict(int)
        for word in words:
            wc[word] += 1
        
        sl = len(words) * len(words[0])
        wl = len(words[0])
        result = []
        
        for i in range(len(s) - sl + 1):
            seen = defaultdict(int)
            for j in range(i, i + sl, wl):
                word = s[j:j+wl]
                if word in wc:
                    seen[word] += 1
                    if seen[word] > wc[word]:
                        break
                else:
                    break
            else:
                result.append(i)
        
        return result
