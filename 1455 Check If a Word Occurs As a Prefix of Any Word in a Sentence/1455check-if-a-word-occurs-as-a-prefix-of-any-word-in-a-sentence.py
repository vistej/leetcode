class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        l = len(searchWord)
        for i in range(len(words)):
            if len(words[i]) >= l and searchWord == words[i][:l]:
                return i + 1
        
        return -1