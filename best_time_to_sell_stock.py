#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(self, prices: List[int]) -> int:
    if len(prices) < 2:
        return 0
    if len(prices) == 2 and prices[0] < prices[1]:
        return prices[1] - prices[0]
    maxPrice = [0 for i in range(len(prices)-1)]
    maxPrice[len(prices)-2] = prices[-1]
    for i in range(len(prices)-3, -1, -1):
        maxPrice[i] = max(maxPrice[i+1], prices[i+1])
        
    maxprofit = 0
        
    for i in range(len(prices)-1):
        prof = maxPrice[i] - prices[i]
        if prof > maxprofit:
            maxprofit=prof
    return maxprofit