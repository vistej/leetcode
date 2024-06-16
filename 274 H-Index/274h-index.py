class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        i = 0
        while citations[i] >= i + 1:
            i += 1
            if i >= len(citations):
                return len(citations)
        return i