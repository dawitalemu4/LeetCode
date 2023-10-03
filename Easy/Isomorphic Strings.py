class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        sM, tM = {}, {}

        for i in range(len(s)):
            if s[i] in sM and sM.get(s[i]) != t[i] or t[i] in tM and tM.get(t[i]) != s[i]:
                return False
            sM[s[i]] = t[i]
            tM[t[i]] = s[i]

        return True