class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        wordsx = [Counter(x) for x in words1]
        words2 = [Counter(x) for x in words2]
        wordsy = defaultdict(int)

        for word in words2:
            for k in word.keys():
                wordsy[k] = max(wordsy[k], word[k])
        

        res = []
        
        for i, w1 in enumerate(wordsx):
            isit = True
            for x in wordsy.keys():
                if x not in w1 or wordsy[x] > w1[x]:
                    isit = False
                    break

            if isit:
                res.append(words1[i])
        
        return res