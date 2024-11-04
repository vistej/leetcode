class Solution:
    def compressedString(self, word: str) -> str:
        last = word[0]
        count = 1
        res = ''

        def addCount(count, res):
            while count:
                if count > 9:
                    res += '9' + last
                    count -= 9
                else:
                    res += str(count) + last
                    count = 0
            return 1, res
        
        for i in range(1, len(word)):
            if word[i] != last:
                count, res = addCount(count, res)
                last = word[i]
            else:
                count += 1
        _, res = addCount(count,res)
        
        return res