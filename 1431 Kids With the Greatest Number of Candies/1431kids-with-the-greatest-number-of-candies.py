class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        cm = 0
        for i in range(len(candies)):
            cm = max(candies[i], cm)
            candies[i] += extraCandies
        for i in range(len(candies)):
            candies[i] = candies[i] >= cm
        return candies
        