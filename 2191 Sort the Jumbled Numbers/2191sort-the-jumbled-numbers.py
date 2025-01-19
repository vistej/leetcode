class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        d = []

        for n in nums:
            k = ''
            x = n
            if not x:
                k = mapping[x]
            else:
                while x:
                    p = x % 10
                    k = str(mapping[p]) + k
                    x = x // 10
            d.append((int(k), n))
        d.sort(key=lambda x: x[0])


        return [x[1] for x in d]