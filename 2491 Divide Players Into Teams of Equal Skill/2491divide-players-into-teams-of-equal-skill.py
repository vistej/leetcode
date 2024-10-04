class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        nt = n // 2

        s = sum(skill)
        ts = s // nt

        skill.sort()

        i = 0
        j = n - 1

        r = 0

        while i < j:
            if skill[i] + skill[j] != ts:
                return -1
            r += skill[i] * skill[j]
            i += 1
            j -= 1
        
        return r