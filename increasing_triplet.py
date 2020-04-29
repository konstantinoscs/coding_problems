# https://leetcode.com/problems/increasing-triplet-subsequence/
def increasingTriplet(self, nums: List[int]) -> bool:
    if not nums:
        return False
    minimum, second_min = sys.maxsize, sys.maxsize
        
    for i in nums:
        if i>second_min:
            return True
        if i>minimum:
            second_min = i
        if i<minimum: #swap but if we run ot of len, still second min is valid*
            minimum = i
            
    return False

#* in array [2,3,1,4] in the end the values will be
# minimum == 1, secondmin == 3
#order is kind of broken but at 4 we still count the 2,3,4 triplet