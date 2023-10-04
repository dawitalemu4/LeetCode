class Solution:
    def isHappy(self, n: int) -> bool:

        while n != 1 and n >= 7:
            s = str(n)
            nxt = 0
            for i in s:
                nxt += int(i) ** 2
            n = nxt

        return n == 1