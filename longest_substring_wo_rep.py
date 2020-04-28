# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# sliding window
def lengthOfLongestSubstring(self, s: str) -> int:
    letters = {}
    start = end = res = 0
    while end<len(s) :
        if s[end] in letters:
            start = max(letters[s[end]], start) #shrink window on repeat
        res = max(res, end-start+1)
        letters[s[end]] = end+1
        #enlarge window
        end+=1
    return res