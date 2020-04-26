//https://leetcode.com/problems/single-number/

func singleNumber(nums []int) int {
    elem :=0
    for _, num := range nums {
        elem = elem ^ num
    }
    return elem
}