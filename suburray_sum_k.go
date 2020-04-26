//https://leetcode.com/problems/subarray-sum-equals-k/
func subarraySum(nums []int, k int) int {
    sums := make(map[int]int)
    res := 0
    sum := 0
    for _, elem := range nums {
        sum += elem
        if sum == k {
            res++
        } 
        if val, found := sums[sum-k]; found {
            res += val
        }
        sums[sum]+=1
    }
    return res
}