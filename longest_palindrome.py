# https://leetcode.com/problems/longest-palindromic-substring/
#dynamic programming
def longestPalindrome(self, s: str) -> str:
    l=2
    palindromes = set()
    maxp = (0,0)
    for i in range(len(s)):
        palindromes.add((i,i))
        if i+1<len(s) and s[i] == s[i+1]:
            palindromes.add((i,i+1))
            maxp = (i,i+1)
                
    for l in range(3,len(s)+1):
        for i in range(0, len(s)-l+1):
            if s[i]== s[i+l-1] and (i+1,i+l-2) in palindromes:
                palindromes.add((i, i+l-1))
                maxp = (i, i+l-1)
    return s[maxp[0]:maxp[1]+1]

# expand around center TODO:
def longestPalindrome(self, s:str) -> str:
    pass