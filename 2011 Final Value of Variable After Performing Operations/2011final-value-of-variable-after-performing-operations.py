class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        r = 0
        for o in operations:
            r += 1 if '+' in o else (-1)
        return r