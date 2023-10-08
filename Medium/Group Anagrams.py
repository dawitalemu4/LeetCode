class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for word in strs:
            s = sorted(word)
            if res.get(str(s)) and word not in res:
                res[str(s)].append(word)
            else:
                res[str(s)] = [word]

        return res.values()