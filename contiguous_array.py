# https://leetcode.com/problems/contiguous-array/
def findMaxLength(self, nums: List[int]) -> int:
    count = 0
    maxi = 0
    sumHash = {}
    for i in range(len(nums)):
        count = count+1 if nums[i] == 0 else count-1
        if count == 0:
            maxi = i+1
        if count not in sumHash:
            sumHash[count] = i
        else:
            maxi = max(maxi, i-sumHash[count])
    return maxi