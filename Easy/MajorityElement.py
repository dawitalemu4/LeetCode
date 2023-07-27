class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        result, maxCounter = 0, 0 

        for n in nums:
            counter[n] = 1 + counter.get(n, 0)
            result = n if counter[n] > maxCounter else result
            maxCounter = max(counter[n], maxCounter)

        return result