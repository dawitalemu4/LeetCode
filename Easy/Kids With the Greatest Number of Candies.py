class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        res, temp, m = [], 0, max(candies)

        for i in range(len(candies)):
            temp = candies[i] + extraCandies
            if temp >= m:
                res.append(True)
            else:
                res.append(False)

        return res