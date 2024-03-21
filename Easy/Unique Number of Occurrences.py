class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        m = {}

        for num in arr:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1

        return len(list(m.values())) == len(set(m.values()))
