class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        nl = sorted(arr)
        diff = nl[1] - nl[0]
        ind = 2
        while ind < len(nl):
            if nl[ind] - nl[ind - 1] != diff:
                return False
            ind += 1
        return True