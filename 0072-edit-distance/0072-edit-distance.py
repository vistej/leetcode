class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}
        
        def getResult(i,j):
            if i == len(word1) and j == len(word2):
                return 0
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i, j) not in dp:
                if word1[i] == word2[j]:
                    ans = getResult(i + 1, j + 1)
                else: 
                    insert = 1 + getResult(i, j + 1)
                    delete = 1 + getResult(i + 1, j)
                    replace = 1 + getResult(i + 1, j + 1)
                    ans = min(insert, delete, replace)
                dp[(i, j)] = ans
            return dp[(i, j)]
        
        return getResult(0,0)