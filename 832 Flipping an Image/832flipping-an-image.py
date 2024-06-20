class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[int(not y) for y in x[::-1]] for x in image]
