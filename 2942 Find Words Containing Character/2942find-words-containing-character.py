class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        r = []
        for i,w in enumerate(words):
            if x in w:
                r.append(i)
        return r