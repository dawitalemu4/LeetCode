class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle not in haystack:
            return -1

        l, r = 0, len(needle)

        while l <= len(haystack):
            window = haystack[l:r]
            if window == needle:
                return l
            l += 1
            r += 1