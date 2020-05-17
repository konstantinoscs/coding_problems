# https://leetcode.com/problems/find-all-anagrams-in-a-string/
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        pletters = Counter(p)
        res = []
        lp = len(p)-1
        sletters = Counter(s[:lp])
        for i in range(len(s)-lp):
            idx = i+lp
            sletters[s[idx]]+=1
            if (sletters == pletters):
                res.append(i)
            sletters[s[i]] -=1
            if sletters[s[i]] == 0:
                del sletters[s[i]]
        
        return res