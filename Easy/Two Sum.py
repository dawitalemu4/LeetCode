class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m = {}

        for i in range(len(nums)):
            if target - nums[i] in m:
                return [m.get(target - nums[i]),i]
            m[nums[i]] = i