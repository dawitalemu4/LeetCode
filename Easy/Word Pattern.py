class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        m = {}
        s = s.split()
        if len(s) != len(pattern):
            return False

        for i in range(len(pattern)):
            if not m.get(s[i]) and pattern[i] not in m.values():
                m[s[i]] = pattern[i]
            elif m.get(s[i]) != pattern[i]:
                return False

        return True 