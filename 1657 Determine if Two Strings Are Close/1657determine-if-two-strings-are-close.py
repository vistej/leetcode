class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wa = {}
        wb = {}

        for w in word1:
            if w not in wa:
                wa[w] = 0
            wa[w] += 1
        
        for w in word2:
            if w not in wb:
                wb[w] = 0
            wb[w] += 1
        
        return wa.keys() == wb.keys() and sorted(wa.values()) == sorted(wb.values())