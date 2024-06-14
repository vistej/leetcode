class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        col = []
        v = {}
        for i,c in enumerate(s):
            v[c] = i
        m = 0
        pm = -1
        print(v)
        for i,c in enumerate(s):
            if v[c] > m:
                m = v[c]
            if i == m:
                col.append(m - pm)
                pm = m
        return col
        
        
