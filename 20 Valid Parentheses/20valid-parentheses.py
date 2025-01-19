class Solution:
    def isValid(self, s: str) -> bool:
        test = []
        for i in s:
            if i in ['(', '{', '[']:
                test.append(i)
            elif i in [')', '}', ']']:
                if len(test):
                    fr = test.pop()
                    if fr + i not in ['()', '{}', '[]']:
                        return False
                else:
                    return False
        return not bool(len(test))