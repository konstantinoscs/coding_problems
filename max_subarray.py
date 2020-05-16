# https://leetcode.com/problems/maximum-subarray/submissions/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsf = nums[0]
        maxeh = nums[0]        
        for i in range(1, len(nums)):
            maxeh = max(maxeh+nums[i], nums[i])
            maxsf = max(maxsf, maxeh)
        return maxsf