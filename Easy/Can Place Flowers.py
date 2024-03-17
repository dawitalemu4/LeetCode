class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        prev = 0

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and prev == 0 and (i+1 == len(flowerbed) or (i+1 < len(flowerbed) and flowerbed[i+1] == 0)):
                flowerbed[i] = 1
                n -= 1
            prev = flowerbed[i]

        return n <= 0
