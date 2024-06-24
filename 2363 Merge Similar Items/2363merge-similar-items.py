class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items1.sort()
        items2.sort()
        r = []
        i = j = 0
        while i < len(items1) and j < len(items2):
            if items1[i][0] > items2[j][0]:
                r.append(items2[j])
                j += 1
            elif items1[i][0] < items2[j][0]:
                r.append(items1[i])
                i += 1
            else:
                r.append([items1[i][0], items2[j][1] + items1[i][1]])
                i += 1
                j += 1
        r.extend(items1[i:])
        r.extend(items2[j:])
        return r