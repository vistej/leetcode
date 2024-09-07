class Solution:
    def missingRolls(self, a: List[int], q: int, n: int) -> List[int]:
        return (n<=(p:=q*(n+len(a))-sum(a))<=n*6)*(p%n*[p//n+1]+(n-p%n)*[p//n])