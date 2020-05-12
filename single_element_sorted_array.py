# https://leetcode.com/problems/single-element-in-a-sorted-array/submissions/
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s, e = 0, len(nums)-1
        while s < e :
            mid = (s+e)//2
            if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]:
                return nums[mid]
            if nums[mid] == nums[mid+1]:
                mid+=1
            if mid == e:
                return nums[mid-2]
            if (e-mid)%2==0:
                e = mid
            else:
                s = mid+1
        
        return nums[s]