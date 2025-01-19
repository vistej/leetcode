class Solution:
    def maxScoreWords(self, words: List[str], ls: List[str], score: List[int]) -> int:
        def loopit(n,l):
            ans = 0
            if n == len(words):
                return 0
            m=l

            for i in words[n]:
                if i not in m:
                    return loopit(n + 1,l)
                m = m.replace(i,'',1)
                ans += score[ord(i)-97]
            return max(loopit(n + 1, l), ans + loopit(n + 1, m))

        return loopit(0,''.join(ls))        