# NeetCode Best Time to Buy And Sell Stock (https://neetcode.io/problems/buy-and-sell-crypto?list=neetcode150)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = int(1e9)
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))  # Output: 5

