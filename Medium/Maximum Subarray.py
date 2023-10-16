class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxSum, curr = min(nums), 0

        for i in range(len(nums)):
            curr = max(nums[i], nums[i] + curr)
            if curr > maxSum:
                maxSum = curr

        return maxSum