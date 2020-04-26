//https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
func maxProfit(prices []int) int {
    var idx, buy, sell, prof = 0, 0, 0, 0
    for idx < len(prices) -1 {
        for idx < len(prices) -1 && prices[idx] >= prices[idx+1] {
            idx ++
        }
        buy = idx
        idx++
        
        for idx < len(prices) && prices[idx-1] <= prices[idx] {
            idx++
        }
        sell = idx -1
        prof += prices[sell] - prices[buy]
    }
    return prof
}