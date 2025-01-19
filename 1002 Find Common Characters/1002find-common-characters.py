class Solution:
    import functools
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        for ch in set(words[0]):
            res += ch * min([word.count(ch) for word in words]) 
        return res