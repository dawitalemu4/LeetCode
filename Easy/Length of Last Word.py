class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        res = ''

        for i in range(len(s)):
            if s[i] != ' ':
                res += s[i]
            elif i + 1 < len(s) and s[i] == ' ' and s[i+1] != ' ': 
                res = ''

        
        return len(res)