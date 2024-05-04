class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lc = 0
        ans = 0

        for row in bank:
            cc = row.count('1')
            if cc:
                if lc:
                    ans += lc * cc

                lc = cc
        return ans