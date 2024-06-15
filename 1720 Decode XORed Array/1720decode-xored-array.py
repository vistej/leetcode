class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        r = [first]
        for n in encoded:
            r.append(r[-1] ^ n)

        return r