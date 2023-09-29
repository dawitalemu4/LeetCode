class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0

        while k < len(nums):
            if nums[k] == val:
                nums.pop(k)
                k -= 1
            k += 1

        return k