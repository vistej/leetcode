class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        k = sorted(intervals, key=lambda x: x[0])
        r = [k[0]]
        j = 1
        while j < len(k):
            if k[j][0] <= r[-1][1]:
                r[-1][1] = max(k[j][1], r[-1][1])
            else:
                r.append(k[j])
            j += 1

        return r
            