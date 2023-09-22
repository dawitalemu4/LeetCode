class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        seen = 0
        k = 1

        while k < len(nums):
            if nums[k] == nums[seen]:
                nums.pop(k)
                k -= 1
            seen = k
            k += 1