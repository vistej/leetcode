class Solution:
    def minOperations(self, s: str) -> int:
        changes01=0
        for i in range(0, len(s)):
            if(int(s[i]) != i%2):
                changes01+=1
        return min(changes01, len(s)-changes01)