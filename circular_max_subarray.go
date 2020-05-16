func maxSubarraySumCircular(A []int) int {
    minus, max := allNeg(A)
    if minus {
        return max
    }
    max_kadane := kadane(A)
    sum_wrap := 0
    for i, elem := range A {
        sum_wrap += elem
        A[i] = -elem
    }
    max_wrap := kadane(A)
    if max_kadane > sum_wrap + max_wrap {
        return max_kadane
    }
    return sum_wrap + max_wrap
}

func kadane(arr []int) int {
    max_here := 0
    max_sf := 0
    for i :=0; i< len(arr); i++ {
        max_here = max(max_here+arr[i], 0)
        max_sf = max(max_sf, max_here)
    }
    return max_sf
}

func allNeg(arr []int) (bool, int) {
    max_elem := arr[0]
    for _, elem := range arr {
        if elem >=0 {
            return false, max_elem
        }
        max_elem = max(max_elem, elem)
    }
    return true, max_elem
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}