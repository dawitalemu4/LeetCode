class Solution:
    def canJump(self, nums: List[int]) -> bool:

        jump, end = nums[0], len(nums) - 1

        for i in range(len(nums)):
            if jump != 0:
                jump -= 1
            if i + 1 < len(nums) and nums[i] > jump:
                jump = nums[i] 
            elif i != end and jump == 0 and nums[i] == 0:
                return False
        
        return True