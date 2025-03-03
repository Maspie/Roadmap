class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        l = 0
        r = l+1
        max_profit = 0
        profit = 0

        
        while r < len(prices):

            if prices[r] - prices[l] < 0:
                l = r
                r+=1
            
            else:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
                r+=1
        return max_profit