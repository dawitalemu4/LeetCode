class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
 
        k = 1

        while k < len(nums):
            if nums[k] == nums[k-1] and k + 1 < len(nums) and nums[k-1] == nums[k+1]: 
                nums.pop(k)
                k -= 1
            k += 1

        # k, seen = 1, 0

        # while k < len(nums):
        #     if nums[k] == nums[seen] and seen + 2 < len(nums) and nums[seen] == nums[seen+2]: 
        #         nums.pop(k)
        #         k -= 1
        #     seen = k
        #     k += 1