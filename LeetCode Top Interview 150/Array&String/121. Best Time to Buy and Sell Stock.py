from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #T=O(n) and S=O(1)
        minPrice=float("inf")# denotes the min price before today
        max_profit=0
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice=prices[i] # the current min price
            elif prices[i]-minPrice>max_profit:
                max_profit=prices[i]-minPrice
        return max_profit







if __name__ == '__main__':
    solution=Solution()
    print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
