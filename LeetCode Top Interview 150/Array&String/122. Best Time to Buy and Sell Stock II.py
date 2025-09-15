from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # T=O(n) S=O(1)
        sum=0
        buyPrice=float("inf")
        for i in range(len(prices)):
            if prices[i]<=buyPrice:# we want to buy the only share of stock at the lowest price
                buyPrice=prices[i]
            elif prices[i]>buyPrice:# means we might sell the stock to gain profit
                if i+1<len(prices) and prices[i+1]>prices[i]:# current time to sell is not the best profit
                    continue
                else:
                    sum+=prices[i]-buyPrice #the best profit
                    buyPrice=float("inf")
        return sum





if __name__ == '__main__':
    solution=Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
