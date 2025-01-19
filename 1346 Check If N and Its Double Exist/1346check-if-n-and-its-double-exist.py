class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set(arr)
        for a in s:
            if (a * 2 in s):
                if a or arr.count(a) > 1:
                    return True
            
        
        return False