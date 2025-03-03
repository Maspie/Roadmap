class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        l = 0  # Buy pointer
        max_profit = 0  # Store max profit

        for r in range(1, len(prices)):  # ✅ Iterate over the prices
            if prices[r] < prices[l]:  # ✅ Found a lower buy price
                l = r  # Update buy pointer
            else:
                max_profit = max(max_profit, prices[r] - prices[l])  # ✅ Directly update max_profit

        return max_profit

