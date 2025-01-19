class Solution:
    def minOperations(self, logs: List[str]) -> int:
        c = 0
        for log in logs:
            if log == "../":
                if c > 0:
                    c -= 1
            elif log == "./":
                continue
            else:
                c += 1
        return c