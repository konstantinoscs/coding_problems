# https://leetcode.com/problems/longest-common-subsequence/
def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    if text1 =="" or text2 =="":
        return 0
    dp = [[0]*(len(text2)+1) for j in range(len(text1)+1)]
    for i in range(len(text1)):
        for j in range(len(text2)):
            dp[i+1][j+1] = 1+dp[i][j] if text2[j] == text1[i] else max(dp[i+1][j], dp[i][j+1])
        
    return dp[-1][-1]