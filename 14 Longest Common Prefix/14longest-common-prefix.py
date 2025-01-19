class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        r = list(strs[0])

        for i in range(1, len(strs)):
            k = []
            s = strs[i]
            for j in range(len(r)):
                if j < len(s) and s[j] == r[j]:
                    k.append(s[j])
                else:
                    break

            if not k:
                return ''
            r = k

        return ''.join(r)