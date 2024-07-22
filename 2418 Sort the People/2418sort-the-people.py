class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        d = []
        for i in range(len(names)):
            d.append((heights[i], names[i]))
        
        d.sort(reverse=True)

        return [k[1] for k in d]