class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        va = version1.split('.')
        vb = version2.split('.')

        i = 0
        while i < max(len(va), len(vb)):
            vai = int(va[i]) if i < len(va) else 0
            vbi = int(vb[i]) if i < len(vb) else 0
            if vai > vbi:
                return 1
            if vbi > vai:
                return -1
            i += 1
        return 0