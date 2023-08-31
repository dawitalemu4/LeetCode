class Solution:
    def reverseWords(self, s: str) -> str:

        res, temp, nextI = '', '', 0
        words = []
        s += ' '
        
        for i in range(len(s)):
            if s[i] != ' ' and i + 1 < len(s):
                temp += s[i]
                nextI = i + 1
                if s[nextI] == ' ' or s[nextI] == '':
                    words.append(temp)
                    temp = ''
            
        for x in range(len(words)):
            res += words[len(words) - 1 - x]
            if x + 1 < len(words):
                res += ' '

        return res