class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        sa = set()
        sb = set()

        res = [0] * len(A)

        for i in range(len(A)):
            res[i] = res[i - 1] if i > 0 else 0
            if A[i] == B[i]:
                res[i] += 1
            else:
                sa.add(A[i])
                sb.add(B[i])
                if A[i] in sb:
                    res[i] += 1
                if B[i] in sa:
                    res[i] += 1
        
        return res
