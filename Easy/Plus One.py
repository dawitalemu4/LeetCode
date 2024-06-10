class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join([str(x) for x in digits])
        plus_one = int(num) + 1
        return [int(x) for x in str(plus_one)]
