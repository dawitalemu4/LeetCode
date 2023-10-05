class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # k % len is the number of elements actually going to move as if you were to iterate k fully  
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        # # Time limit exceeded on big input but correct      
        # while k != 0:
        #     nums[:] = nums[-1:] + nums[:-1] 
        #     k -= 1

        #Iterative
        # while k != 0:
        #     nums.insert(0, nums[len(nums) - 1])
        #     nums.pop()
        #     k -= 1