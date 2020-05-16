# https://leetcode.com/problems/search-in-rotated-sorted-array/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (end-start)//2 + start
            diff = target - nums[mid]
            if diff ==0:
                return mid
            elif diff > 0:
                if target> nums[end] and nums[end] > nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            else:
                if target < nums[start] and nums[start] <= nums[mid]:
                    start = mid+1
                else:
                    end = mid-1
        return start if start==end and nums[start] == target else -1