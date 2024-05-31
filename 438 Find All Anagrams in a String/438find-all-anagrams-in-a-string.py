class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pd = {}
        for i in p:
            pd[i] = pd.get(i, 0) + 1
        sd = {}
        r = []
        l = len(p)
        for i in range(len(s)):
            sd[s[i]] = sd.get(s[i], 0) + 1
            if i >= l - 1:
                if pd == sd:
                    r.append(i - l + 1)
                sd[s[i - l + 1]] -= 1
                if not sd[s[i - l + 1]]:
                    del sd[s[i - l + 1]]
        return r