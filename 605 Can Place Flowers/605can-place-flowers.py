class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i]:
                continue
            if i - 1 >= 0 and flowerbed[i - 1]:
                continue
            if i + 1 < len(flowerbed) and flowerbed[i + 1]:
                continue
            flowerbed[i] = 1
            n -= 1
            if not n:
                return True
        return n == 0            
