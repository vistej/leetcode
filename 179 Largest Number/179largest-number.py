import functools

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def check(a, b):
            if a + b > b + a:
                return -1
            else:
                return 1
            

        x = [str(v) for v in nums]
        x.sort(key=functools.cmp_to_key(check))

        r = ''.join(x)
        if r[0] == '0':
            return '0'
        
        return r