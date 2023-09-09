class Solution:
    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        maxH = (r - l) * min(height[l], height[r])

        while l < r:
            if height[l] > height[r]:
                r -= 1
            elif height[r] < height[l]:
                l += 1
            else:
                l += 1
            if maxH < (r - l) * min(height[l], height[r]):
                maxH = (r - l) * min(height[l], height[r])

        return maxH