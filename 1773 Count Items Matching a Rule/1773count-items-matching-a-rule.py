class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d = {'type': 0, 'color': 1, 'name': 2}
        c = 0
        for it in items:
            c +=  int(it[d[ruleKey]] == ruleValue)

        return c